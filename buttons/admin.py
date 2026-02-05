from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


async def accept_decline_kb(type_data, data):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Accept ✅", callback_data=f"accept_{type_data}_{data}"),
            InlineKeyboardButton(text="Decline ❌", callback_data=f"decline_{type_data}_{data}"),
        ],
    ])
    return kb


async def admin_menu_bt():
    bt = ReplyKeyboardBuilder()

    bt.row(KeyboardButton(text="Championship MGMT"))
    bt.row(KeyboardButton(text="Essay MGMT"))
    bt.row(KeyboardButton(text="User MGMT"))
    bt.row(KeyboardButton(text="◀️ Back"))

    b = bt.as_markup()
    b.resize_keyboard=True
    return b


async def event_mgmt_kb():
    kb = InlineKeyboardBuilder()

    kb.row(
        InlineKeyboardButton(text="Add", callback_data=f"event_mgmt_add"),
        InlineKeyboardButton(text="Edit", callback_data=f"event_mgmt_edit"),
    )
    kb.row(
        InlineKeyboardButton(text="Delete", callback_data=f"event_mgmt_delete"),
        InlineKeyboardButton(text="Deactivate", callback_data=f"event_mgmt_deactivate"),
    )
    kb.row(InlineKeyboardButton(text="◀️ Back", callback_data=f"admin_menu"))

    b = kb.as_markup()
    return b
