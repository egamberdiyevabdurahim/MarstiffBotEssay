import datetime

from aiogram import types, Router, F
from aiogram.fsm.context import FSMContext

from buttons.admin import event_mgmt_kb
from buttons.user import times_kb
from database_config.config import ADMINISTRATION_GROUP_ID
from filters.role import RoleFilter
from states.admin import CreateEventSt
from utils.additions import MESSAGE_EFFECTS
from utils.reply_keyboard_rm import reply_keyboard_rm
from utils.validator import vld

from loader import _, Event, bot

router = Router()


@router.message(F.text=="Championship MGMT", RoleFilter([0]))
async def championship_mgmt_f(mess: types.Message, u=None):
    await vld(o=mess, u=u or mess.from_user, delete=False if u else True)
    await reply_keyboard_rm(mess=mess)

    text=_("Championship MGMT") + " 👇"
    markup = await event_mgmt_kb()
    try:
        await mess.edit_text(
            text=text,
            reply_markup=markup,
            parse_mode='HTML'
        )
    except Exception:
        await mess.answer(
            text=text,
            reply_markup=markup,
            parse_mode='HTML'
        )


@router.callback_query(F.data == "event_mgmt_add", RoleFilter([0]))
async def event_mgmt_add_f(call: types.CallbackQuery, state: FSMContext):
    await vld(o=call, u=call.from_user)

    await call.message.edit_text(
        text="Enter name for event:",
        reply_markup=None,
        parse_mode='HTML'
    )
    await state.set_state(CreateEventSt.name)


@router.message(CreateEventSt.name)
async def event_mgmt_add_name_f(mess: types.Message, state: FSMContext):
    await vld(o=mess, u=mess.from_user)

    await state.update_data(name=mess.text)
    await mess.answer(
        text="Enter cost for event:",
        parse_mode='HTML'
    )
    await state.set_state(CreateEventSt.cost)


@router.message(CreateEventSt.cost)
async def event_mgmt_add_cost_f(mess: types.Message, state: FSMContext):
    await vld(o=mess, u=mess.from_user)

    await state.update_data(cost=mess.text)
    await mess.answer(
        text="📅 Enter date for event (DD.MM.YYYY):"
    )
    await state.set_state(CreateEventSt.date)


@router.message(CreateEventSt.date)
async def event_mgmt_add_date_f(mess: types.Message, state: FSMContext):
    await vld(o=mess, u=mess.from_user)

    try:
        selected_date = datetime.datetime.strptime(
            mess.text.strip(),
            "%d.%m.%Y"
        ).date()
    except ValueError:
        await mess.answer("❌ Wrong format. Use DD.MM.YYYY\nPlease try again.")
        return await state.set_state(CreateEventSt.date)

    await mess.answer(
        text="⏰ Choose time:",
        reply_markup=await times_kb(selected_date=selected_date)
    )

    await state.set_state(CreateEventSt.hour)


@router.callback_query(CreateEventSt.hour)
async def event_mgmt_add_hour_f(call: types.CallbackQuery, state: FSMContext):
    await vld(o=call, u=call.from_user, delete=True)

    await state.update_data(starting_date=call.data)
    await call.message.answer(
        text="Send a video"
    )
    await state.set_state(CreateEventSt.video)


@router.message(CreateEventSt.video, F.video)
async def event_mgmt_add_video_f(mess: types.Message, state: FSMContext):
    u_d = await vld(o=mess, u=mess.from_user)

    st_data = await state.get_data()
    name = st_data.get("name")
    cost = st_data.get("cost")
    starting_date = st_data.get("starting_date")
    starting_date = datetime.datetime.strptime(starting_date, "%Y-%m-%d %H:%M")
    video = mess.video.file_id

    section = await bot.create_forum_topic(
        chat_id=ADMINISTRATION_GROUP_ID,
        name=name,
    )

    await Event.create(
        name=name,
        cost=cost,
        starting_date=starting_date,
        video=video,
        section=section.message_thread_id,
        created_by=u_d.idn,
    )

    await mess.answer(
        text="Congrats 🎉. You have created new CHAMPIONSHIP\n\n"
             f"Name: {name}\n"
             f"Cost: {cost}\n"
             f"Starting_date: {starting_date}\n",
        message_effect_id=MESSAGE_EFFECTS["🎉"]
    )
    await state.clear()
    await championship_mgmt_f(mess=mess, u=mess.from_user)
