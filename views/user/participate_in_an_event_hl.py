from aiogram import types, Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import InputMediaVideo

from buttons.admin import accept_decline_kb
from buttons.main import cancel_pay_later_kb
from buttons.user import events_kb
from database_config.config import ADMINISTRATION_GROUP_ID
from loader import _, Essentials, Event, EventUser, TGGroup, TGGroupSection, bot
from states.user import ParticipateInAnEventSt
from utils.additions import MESSAGE_EFFECTS
from utils.message_linker import message_linker
from utils.notifier import notice_main_group
from utils.reply_keyboard_rm import reply_keyboard_rm
from utils.validator import vld

router = Router()


@router.message(F.text=="Championship 🏆")
async def participate_in_an_event_f(mess: types.Message, u=None, page=1):
    u, delete = u or mess.from_user, False if u else True
    u_d = await vld(o=mess, u=u)
    events = await Event.get_all_actives()
    if len(events)>0:
        if delete:
            await reply_keyboard_rm(mess=mess)

        data = events[page-1]
        previous_pg = page-1 if events[page-2] else None
        next_pg = page+1 if events[-1]!=data else None
        participant = False
        if await EventUser.get_data_by_event_u(event=data.idn, u=u_d.idn):
            participant = True
        markup = await events_kb(
                    u=u,
                    lang=u.language_code,
                    data=data,
                    page=page,
                    previous_pg=previous_pg,
                    next_pg=next_pg,
                    participant=participant,
                )
        text = (f"<b>{data.name}</b>: {data.cost}\n"+
                _(f"When")+f": {data.starting_date.strftime('%d.%m.%Y %H:%M')}\n"+
                _(f'<b>{"You are already a participant" if participant is True else "You have not participated yet"}</b>'))

        try:
            await mess.edit_media(
                reply_markup=markup,
                media=InputMediaVideo(
                    media=data.video,
                    caption=text,
                    parse_mode="HTML",
                ),
                parse_mode="HTML"
            )

        except Exception:
            await mess.answer_video(
                caption=text,
                reply_markup=markup,
                video=data.video,
                parse_mode="HTML"
            )

    else:
        await mess.reply(
            text=_("Unfortunately, there is no event right now") + " 😢",
        )


@router.callback_query(F.data.startswith("participate_"))
async def participate_in_an_event_payment_f(call: types.CallbackQuery, state: FSMContext):
    __, data = call.data.split("_", 1)
    type_d, participant, data = data.split(":", 2)
    u = call.from_user

    if type_d == "event":
        if participant != "False":
            await vld(
                o=call,
                u=call.from_user,
                ans_mg=_("You are already participating in this event") + " 😃",
                show_alert=True
            )

        else:
            await vld(o=call, u=call.from_user, delete=True)
            event = await Event.get_data(idn=data)
            card = await Essentials.get_by_key(key="credit_card")
            text = (_(f"<b>Great</b>, now you should pay: <b>{event.cost}</b> to participate in this event")+"\n"+
                    _(f"Believe me, it's going to be your best <b>investment</b> for yourself")+" 😉\n\n"+
                    _("Card number")+f": <code>{card.val}</code>\n\n"+
                    _("After payment, you should send proof. It can be cheque image/file"))
            markup = await cancel_pay_later_kb(lang=call.from_user.language_code, ex="participate_in_an_event_f")

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
            await state.update_data(idn=event.idn)
            await state.set_state(ParticipateInAnEventSt.proof)


@router.message(ParticipateInAnEventSt.proof)
async def participate_in_an_event_proof_f(mess: types.Message, state: FSMContext):
    u = mess.from_user
    u_d = await vld(o=mess, u=u)

    st_data = await state.get_data()
    event_idn = st_data.get("idn")
    event = await Event.get_data(idn=event_idn)
    group = await TGGroup.get_by_chat_id(chat_id=ADMINISTRATION_GROUP_ID)
    section = await TGGroupSection.get_data_by_type_connected_group(group_idn=group.idn, type_connected=4)
    caption = (f"<b>{u_d.name} | {u_d.id_name}</b> wants to participate in this event: <b>{event.name}</b> and paid <b>{event.cost}</b>.\n\n"
               f"Here is the cheque. Will you accept?")
    markup = await accept_decline_kb(type_data="event", data=f"{event.idn}:{u_d.idn}")
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
        return await state.set_state(ParticipateInAnEventSt.proof)

    await notice_main_group(
        message=f"📌 We have a new payment for an event, don't forget to accept or decline — {await message_linker(mess=data)}",
        section=0
    )

    data2 = await bot.send_message(
        chat_id=group.group_id,
        message_thread_id=event.section,
        text=f"📌 We have a new request, he/she haven't paid yet or in process\n\n"
                f"ID: {u_d.id_name}\n"
                f"Name: {u_d.name}\n"
                f"Phone: {u_d.phone_number}\n"
    )

    await mess.answer(
        text=_("Great, now your payment is being checked (it can last a lot)")
    )
    await EventUser.create(
        event_idn=event_idn,
        u_idn=u_d.idn,
        paid=0,
        in_process=1,
        message_id=data.message_id,
        message_id2=data2.message_id,
        proof=proof,
        amount=event.cost,
    )
    return None