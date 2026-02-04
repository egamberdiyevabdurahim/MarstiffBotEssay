from aiogram import types, Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from buttons.user import services_menu_bt
from filters.role import RoleFilter
from utils.message_deleter import message_deleter
from utils.validator import vld
from views.user.participate_in_an_event_hl import participate_in_an_event_f

from loader import _

router = Router()


@router.message(F.text=="Services 📣", RoleFilter([1]))
async def services_menu_f(mess: types.Message, u=None):
    u_d = await vld(o=mess, u=u or mess.from_user)

    text=_("Choose") + " 👇"
    markup = await services_menu_bt(u=u_d, lang=u_d.lang)
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


@router.callback_query(F.data == "services", RoleFilter([1]))
async def services_menu_caller_f(call: CallbackQuery, state: FSMContext):
    await state.clear()
    await message_deleter(u_id=call.from_user.id, message_id=call.message.message_id)
    await services_menu_f(mess=call.message, u=call.from_user)


@router.callback_query(F.data.startswith("pager_"), RoleFilter([1]))
async def pager_f(call: types.CallbackQuery):
    await vld(o=call, u=call.from_user)
    __, data = call.data.split("_", 1)
    type_d, data = data.split(":", 1)

    if type_d == "event":
        await participate_in_an_event_f(
            mess=call.message,
            u=call.from_user,
            page=int(data),
        )
