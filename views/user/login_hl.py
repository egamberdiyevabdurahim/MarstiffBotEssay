from aiogram import types, Router
from aiogram.fsm.context import FSMContext

from buttons.main import send_phone_kb
from buttons.user import start_menu_bt
from loader import User, _, Balance
from states.user import FillingDataSt
from utils.additions import MESSAGE_EFFECTS
from utils.id_name_generator import id_name_generator
from utils.message_linker import message_linker
from utils.notifier import notice_main_group
from utils.validator import vld

router = Router()


async def create_user_f(mess: types.Message, state: FSMContext, u=None):
    u_d = await vld(o=mess, u=u)
    if not u_d:
        await mess.answer(
            text=_("Please enter your fullname (name surname)")
        )
        await state.set_state(FillingDataSt.name)


@router.message(FillingDataSt.name)
async def create_user_name_f(mess: types.Message, state: FSMContext):
    await vld(o=mess, u=mess.from_user)
    await mess.answer(
        text=_("Great, now please enter your age", locale=mess.from_user.language_code) + ":"
    )
    await state.update_data(name=mess.text)
    await state.set_state(FillingDataSt.age)


@router.message(FillingDataSt.age)
async def create_user_age_f(mess: types.Message, state: FSMContext):
    await vld(o=mess, u=mess.from_user)
    data = mess.text
    if not data.isdigit():
        await mess.answer(text=_("Oops, you sent me wrong data. Please send me your age")+"!")
        return await state.set_state(FillingDataSt.age)

    elif 7 > int(data) > 50:
        await mess.answer(text=_("Oops, you sent me wrong data. Please send me your exact age")+".!\n"+
                               _("I know you aren't at that age")+" 🙄")
        return await state.set_state(FillingDataSt.age)

    await mess.answer(
        text=_("Great, now please enter your phone number", locale=mess.from_user.language_code) + ":",
        reply_markup=await send_phone_kb(lang=mess.from_user.language_code)
    )
    await state.update_data(age=int(mess.text))
    return await state.set_state(FillingDataSt.phone)


@router.message(FillingDataSt.phone)
async def create_user_phone_f(mess: types.Message, state: FSMContext):
    u = mess.from_user
    u_d = await vld(o=mess, u=u)
    phone = mess.contact.phone_number if mess.contact else mess.text
    st_data = await state.get_data()
    name = st_data.get("name")
    age = st_data.get("age")

    await state.clear()
    await mess.answer(
        text=_("Congrats")+" 🎉 "+_("You have successfully logged in")+".",
        message_effect_id=MESSAGE_EFFECTS["🎉"]
    )
    id_name = await id_name_generator()
    await User.create(
        id_name=id_name,
        chat_id=u.id,
        tg_username=u.username,
        tg_first_name=u.first_name,
        tg_last_name=u.last_name,
        lang="en",
        name=name,
        age=age,
        phone_number=phone
    )
    data = await notice_main_group(
        message=("<b>🚀 New comer in Telegram bot</b>\n\n"
                 f"<b>ID:</b> {id_name}\n"
                 f"<b>Name:</b> {name}\n"
                 f"<b>TG First Name:</b> {u.first_name}\n"
                 f"<b>TG Last Name:</b> {u.last_name or 'BLANK'}\n"
                 f"<b>Age:</b> {age}\n"
                 f"<b>Phone Number:</b> {phone}\n"
                 f"<b>ChatID:</b> {u.id}\n"
                 + (
                 f"<b>Username:</b> @{u.username}" if u.username else "<b>Username:</b> BLANK")),
        section=1,
    )
    u_d = await User.get_data(chat_id=u.id)
    await Balance.create(
        u_idn=u_d.idn,
        amount=0,
        is_benefit=1,
    )
    await notice_main_group(
        message=f"📌 We have a new comer — {await message_linker(mess=data)}",
        section=0
    )

    text = ("Assalamu Alaykum\n" +
            _("Welcome to Marstiff's official bot.") + "\n" +
            _("Choose") + " 👇")
    markup = await start_menu_bt(u=u_d or u, lang=u.language_code)
    await mess.answer(
        text=text,
        reply_markup=markup,
        parse_mode='HTML'
    )