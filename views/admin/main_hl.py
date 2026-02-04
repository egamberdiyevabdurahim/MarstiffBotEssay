from aiogram import types, Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from buttons.admin import admin_menu_bt
from buttons.user import services_menu_bt
from filters.role import RoleFilter
from utils.message_deleter import message_deleter
from utils.validator import vld
from views.user.participate_in_an_event_hl import participate_in_an_event_f

from loader import _

router = Router()


@router.message(F.text=="Admin panel 💎", RoleFilter([0]))
async def admin_menu_f(mess: types.Message, u=None):
    await vld(o=mess, u=u or mess.from_user, delete=True if u else False)

    text=_("Choose") + " 👇"
    markup = await admin_menu_bt()
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


@router.callback_query(F.data == "admin_menu", RoleFilter([0]))
async def admin_menu_caller_f(call: types.CallbackQuery, state: FSMContext):
    await state.clear()
    await admin_menu_f(mess=call.message, u=call.from_user)
