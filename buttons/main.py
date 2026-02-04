from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup

from loader import _


async def confirm_kb(lang, ex=""):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text=_("Confirm", locale=lang), callback_data=f"confirm{ex}")
        ]
    ])
    return kb


async def cancel_pay_later_kb(lang, ex=""):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text=_("Cancel", locale=lang)+" ❌", callback_data=f"cancel_{ex}")
        ]
    ])
    return kb


async def send_phone_kb(lang):
    bt = ReplyKeyboardMarkup(keyboard=[
        [
            KeyboardButton(
                text=_("Send phone number", locale=lang)+" 📞",
                request_contact=True,
            )
        ]
    ],
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder=_("Ex: +998991234567", locale=lang)+" 📞"
    )
    return bt
