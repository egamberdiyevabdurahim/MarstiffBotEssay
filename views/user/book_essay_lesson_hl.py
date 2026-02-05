from datetime import datetime

from aiogram import types, Router, F
from aiogram.fsm.context import FSMContext

from buttons.admin import accept_decline_kb
from buttons.main import cancel_pay_later_kb
from buttons.user import understood_kb, dates_kb, times_kb
from database_config.config import ADMINISTRATION_GROUP_ID
from loader import _, Essentials, Essay, TGGroup, TGGroupSection, bot, EssayUser, User
from states.user import BookEssaySt
from utils.additions import MESSAGE_EFFECTS
from utils.message_linker import message_linker
from utils.notifier import notice_main_group
from utils.reply_keyboard_rm import reply_keyboard_rm
from utils.validator import vld

router = Router()


@router.message(F.text=="Essay 📝")
async def book_essay_f(mess: types.Message):
    u = mess.from_user
    u_d = await vld(o=mess, u=u)
    await reply_keyboard_rm(mess=mess)
    video = await Essay.get_active()
    await mess.answer_video(
        caption=_("It's an instruction video. After watching video, tap the button below"),
        video=video.video,
        reply_markup=await understood_kb(lang=u_d.lang),
    )


@router.callback_query(F.data == "book_essay")
async def book_essay_date_f(call: types.CallbackQuery, state: FSMContext):
    u = call.from_user
    u_d = await User.get_data(chat_id=u.id)
    data = await Essay.get_active()
    dat = await EssayUser.get_data_by_essay_u(essay=data.idn, u=u_d.idn)
    if not dat:
        await vld(o=call, u=u, delete=True)
        await call.message.answer(
            text=_("Great, please choose the day when you want to book") + " :",
            reply_markup=await dates_kb()
        )
        await state.set_state(BookEssaySt.date)

    else:
        await vld(
            o=call,
            u=call.from_user,
            ans_mg=_("You have already active essay") + " 😃",
            show_alert=True
        )


@router.callback_query(BookEssaySt.date)
async def book_essay_time_f(call: types.CallbackQuery, state: FSMContext):
    u = call.from_user
    await vld(o=call, u=u)
    try:
        await call.message.edit_text(
            text=_("Great, please choose time when you want to book") + " :",
            reply_markup=await times_kb(selected_date=call.data)
        )
    except Exception:
        await call.message.answer(
            text=_("Great, please choose time when you want to book") + " :",
            reply_markup=await times_kb(selected_date=call.data)
        )
    await state.update_data(day=call.data)
    await state.set_state(BookEssaySt.time)


@router.callback_query(BookEssaySt.time)
async def book_essay_payment_f(call: types.CallbackQuery, state: FSMContext):
    u = call.from_user
    await vld(o=call, u=u)
    await state.update_data(hour=call.data)

    essay = await Essay.get_active()
    card = await Essentials.get_by_key(key="credit_card")
    text = (_(f"<b>Great</b>, now you should pay: <b>{essay.cost}</b> to book essay zoom") + "\n" +
            _(f"Believe me, it's going to be your best <b>investment</b> for yourself") + " 😉\n\n" +
            _("Card number") + f": <code>{card.val}</code>\n\n" +
            _("After payment, you should send proof. It can be cheque image/file"))
    markup = await cancel_pay_later_kb(lang=call.from_user.language_code, ex="essay")

    try:
        await call.message.edit_text(
            text=text,
            reply_markup=markup,
            parse_mode="HTML",
            message_effect_id=MESSAGE_EFFECTS["🔥"],
        )

    except Exception:
        await call.message.answer(
            text=text,
            reply_markup=markup,
            parse_mode="HTML",
            message_effect_id=MESSAGE_EFFECTS["🔥"],
        )
    await state.update_data(idn=essay.idn)
    await state.set_state(BookEssaySt.proof)


@router.message(BookEssaySt.proof)
async def book_lesson_proof_f(mess: types.Message, state: FSMContext):
    u = mess.from_user
    u_d = await vld(o=mess, u=u)

    st_data = await state.get_data()
    hour = st_data.get("hour")
    essay = await Essay.get_active()
    group = await TGGroup.get_by_chat_id(chat_id=ADMINISTRATION_GROUP_ID)
    section = await TGGroupSection.get_data_by_type_connected_group(group_idn=group.idn, type_connected=4)
    caption = (
        f"<b>{u_d.name} | {u_d.id_name}</b> wants to book an essay zoom at {hour} and paid <b>{essay.cost}</b>.\n\n"
        f"Here is the cheque. Will you accept?")
    markup = await accept_decline_kb(type_data="essay", data=f"{essay.idn}:{u_d.idn}")
    if mess.photo:
        data = await bot.send_photo(
            chat_id=group.group_id,
            message_thread_id=section.section_id,
            caption=caption,
            photo=mess.photo[-1].file_id,
            reply_markup=markup,
            parse_mode="HTML",
        )
        proof = mess.photo[-1].file_id

    elif mess.document:
        data = await bot.send_document(
            chat_id=group.group_id,
            message_thread_id=section.section_id,
            caption=caption,
            document=mess.document.file_id,
            reply_markup=markup,
            parse_mode="HTML",
        )
        proof = mess.document.file_id

    else:
        await mess.reply(
            text=_("Oops, something went wrong. Please try again."),
        )
        return await state.set_state(BookEssaySt.proof)

    await notice_main_group(
        message=f"📌 We have a new payment, don't forget to accept or decline — {await message_linker(mess=data)}",
        section=0
    )
    data2 = await bot.send_message(
        chat_id=group.group_id,
        message_thread_id=essay.section,
        text=f"📌 We have a new request, he/she haven't paid yet or in process\n\n"
                f"ID: {u_d.id_name}\n"
                f"Name: {u_d.name}\n"
                f"Phone: {u_d.phone_number}\n"
    )

    await mess.answer(
        text=_("Great, now your payment is being checked (it can last a lot)")
    )

    starting_date = datetime.strptime(hour, "%Y-%m-%d %H:%M")
    await EssayUser.create(
        essay_idn=essay.idn,
        u_idn=u_d.idn,
        paid=0,
        in_process=1,
        starting_date=starting_date,
        message_id=data.message_id,
        message_id2=data2.message_id,
        proof=proof,
        amount=essay.cost,
    )
    return None
