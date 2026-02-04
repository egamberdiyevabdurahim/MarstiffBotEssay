from aiogram import types, Router, F

from database_config.config import ADMINISTRATION_GROUP_ID
from filters.role import RoleFilter
from utils.message_linker import message_linker
from utils.validator import vld

from loader import EventUser, EssayUser, Transaction, Balance, bot, TGGroup, TGGroupSection, Event, User

router = Router()


@router.callback_query(F.data.startswith("accept_"), RoleFilter([0]))
async def accept_f(call: types.CallbackQuery, u=None):
    u_d = await vld(o=call, u=u or call.from_user)
    __, type_data, idn = call.data.split("_", 2)
    data_idn, u_par_idn = idn.split(":", 1)

    group = await TGGroup.get_by_chat_id(chat_id=ADMINISTRATION_GROUP_ID)
    section = await TGGroupSection.get_data_by_type_connected_group(group_idn=group.idn, type_connected=2)
    u_par = await User.get_by_idn(idn=u_par_idn)

    data, caption, text2 = None, None, None

    if type_data == "event":
        event = await Event.get_data(idn=data_idn)
        data = await EventUser.get_data_by_event_u(event=data_idn, u=u_par_idn)

        balance = await Balance.get_by_u(u=u_par_idn)
        await Transaction.create(
            balance_idn=balance.idn,
            amount=data.amount,
            is_benefit=0,
            proof=data.proof,
            for_what="event",
            for_what_idn=data.event_idn,
        )

        caption = (
            f"<b>{u_par.name} | {u_par.id_name}</b> wanted to participate in this event: <b>{event.name}</b> and paid <b>{data.amount}</b>.\n\n"
            f"Here is the cheque. Accepted by --> <b>{u_d.name}</b>")

        text2 = f"Your payment for {event.name} has been accepted!"

    elif type_data == "essay":
        data = await EssayUser.get_data_by_essay_u(essay=data_idn, u=u_par_idn)

        balance = await Balance.get_by_u(u=u_par_idn)
        await Transaction.create(
            balance_idn=balance.idn,
            amount=data.amount,
            is_benefit=0,
            proof=data.proof,
            for_what="essay",
            for_what_idn=data.essay_idn,
        )

        caption = (
            f"<b>{u_par.name} | {u_par.id_name}</b> wanted to book an essay zoom at {data.starting_date} and paid <b>{data.amount}</b>.\n\n"
            f"Here is the cheque. Accept by --> <b>{u_d.name}</b>")

        text2 = "Your payment for essay has been accepted!"

    data.in_process = 0
    data.paid = 1
    await data.save()
    await bot.edit_message_caption(
        chat_id=group.group_id,
        message_id=data.message_id,
        caption=caption,
        parse_mode="HTML",
        reply_markup=None
    )
    try:
        mess_d = await bot.send_photo(
            chat_id=group.group_id,
            message_thread_id=section.section_id,
            caption=caption,
            photo=data.proof,
            parse_mode="HTML",
        )
    except Exception:
        mess_d = await bot.send_document(
            chat_id=group.group_id,
            message_thread_id=section.section_id,
            caption=caption,
            document=data.proof,
            parse_mode="HTML",
        )

    text = (
        f"📌 We had a new request, he/she paid --> "
        f"<b><a href='{await message_linker(mess=mess_d)}'>CHEQUE</a></b>\n\n"
        f"ID: {u_par.id_name}\n"
        f"Name: {u_par.name}\n"
        f"Phone: {u_par.phone_number}\n"
    )
    await bot.edit_message_text(
        chat_id=group.group_id,
        message_id=data.message_id2,
        text=text,
        parse_mode="HTML",
    )
    await bot.send_message(
        chat_id=u_par.chat_id,
        text=text2+f"\n<b>{u_par.id_name}</b> 👈 Your ID. You will enter with this.",
        parse_mode="HTML",
    )


@router.callback_query(F.data.startswith("decline_"), RoleFilter([0]))
async def decline_f(call: types.CallbackQuery, u=None):
    u_d = await vld(o=call, u=u or call.from_user)
    __, type_data, idn = call.data.split("_", 2)
    data_idn, u_par_idn = idn.split(":", 1)

    group = await TGGroup.get_by_chat_id(chat_id=ADMINISTRATION_GROUP_ID)
    section = await TGGroupSection.get_data_by_type_connected_group(group_idn=group.idn, type_connected=3)
    u_par = await User.get_by_idn(idn=u_par_idn)

    data, caption, text2 = None, None, None

    if type_data == "event":
        event = await Event.get_data(idn=data_idn)
        data = await EventUser.get_data_by_event_u(event=data_idn, u=u_par_idn)

        caption = (
            f"<b>{u_par.name} | {u_par.id_name}</b> wanted to participate in this event: <b>{event.name}</b> and couldn't paid <b>{data.amount}</b>.\n\n"
            f"Here is the cheque. Declined by --> <b>{u_d.name}</b>")

        text2 = f"Your payment for {event.name} has been declined!"

    elif type_data == "essay":
        data = await EssayUser.get_data_by_essay_u(essay=data_idn, u=u_par_idn)

        caption = (
            f"<b>{u_par.name} | {u_par.id_name}</b> wanted to book an essay zoom at {data.starting_date} and couldn't paid <b>{data.amount}</b>.\n\n"
            f"Here is the cheque. Declined by --> <b>{u_d.name}</b>")

        text2 = f"Your payment for essay has been declined!"

    data.in_process = 0
    data.paid = 0
    data.active = 0
    await data.save()
    await bot.edit_message_caption(
        chat_id=group.group_id,
        message_id=data.message_id,
        caption=caption,
        parse_mode="HTML",
        reply_markup=None
    )
    try:
        mess_d = await bot.send_photo(
            chat_id=group.group_id,
            message_thread_id=section.section_id,
            caption=caption,
            photo=data.proof,
            parse_mode="HTML",
        )
    except Exception:
        mess_d = await bot.send_document(
            chat_id=group.group_id,
            message_thread_id=section.section_id,
            caption=caption,
            document=data.proof,
            parse_mode="HTML",
        )

    text = (
        f"📌 We had a new request, he/she couldn't paid --> "
        f"<b><a href='{await message_linker(mess=mess_d)}'>CHEQUE</a></b>\n\n"
        f"ID: {u_par.id_name}\n"
        f"Name: {u_par.name}\n"
        f"Phone: {u_par.phone_number}\n"
    )
    await bot.edit_message_text(
        chat_id=group.group_id,
        message_id=data.message_id2,
        text=text,
        parse_mode="HTML",
    )
    await bot.send_message(
        chat_id=u_par.chat_id,
        text=text2,
        parse_mode="HTML",
    )