from datetime import timedelta

from aiogram.types import KeyboardButton, InlineKeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

from loader import _
from utils.additions import tas_t


async def start_menu_bt(u, lang):
    bt = ReplyKeyboardBuilder()

    if u.role == 0:
        bt.row(KeyboardButton(text=_("Admin panel", locale=u.lang) + " 💎"))

    elif u.role == 1:
        bt.row(KeyboardButton(text=_("Services", locale=lang) + " 📣"))
        bt.row(KeyboardButton(text=_("Profile", locale=lang) + " 👤"))

    b = bt.as_markup()
    b.resize_keyboard=True
    return b


async def services_menu_bt(u, lang):
    bt = ReplyKeyboardBuilder()

    if u.role == 1:
        bt.row(KeyboardButton(text=_("Championship", locale=lang) + " 🏆"))
        bt.row(KeyboardButton(text=_("Essay", locale=lang) + " 📝"))
        bt.row(KeyboardButton(text="◀️ " + _("Back", locale=lang)))

    b = bt.as_markup()
    b.resize_keyboard=True
    return b


async def understood_kb(lang):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text=_("I’ve gone through it", locale=lang)+" ✅", callback_data=f"book_essay"),
        ],
        [
            InlineKeyboardButton(text="◀️ " + _("Back", locale=lang), callback_data=f"services"),
        ],
    ])
    return kb


async def events_kb(u, lang, data, page=1, previous_pg=None, next_pg=None, participant=None):
    kb = InlineKeyboardBuilder()
    if not participant:
        kb.row(InlineKeyboardButton(
            text=_("Participate", locale=lang) + " 😎",
            callback_data=f"participate_event:{participant}:{data.idn}"
        ))
    nav_buttons = []

    if previous_pg:
        nav_buttons.append(
            InlineKeyboardButton(text="◀️", callback_data=f"pager_event:{previous_pg}")
        )

    nav_buttons.append(
        InlineKeyboardButton(text=str(page), callback_data="nothing")
    )

    if next_pg:
        nav_buttons.append(
            InlineKeyboardButton(text="▶️", callback_data=f"pager_event:{next_pg}")
        )

    kb.row(*nav_buttons)
    kb.row(InlineKeyboardButton(text="◀️ "+_("Back", locale=lang), callback_data=f"services"))
    b = kb.as_markup()
    return b


async def dates_kb():
    kb = InlineKeyboardBuilder()
    now = tas_t()

    start_date = now
    if now.hour > 18:
        start_date += timedelta(days=1)

    for i in range(8):
        d = start_date + timedelta(days=i)
        kb.add(
            InlineKeyboardButton(
                text=d.strftime("%d %b"),
                callback_data=f"{d.date()}"
            )
        )

    kb.adjust(3)
    return kb.as_markup()


async def times_kb(selected_date):
    kb = InlineKeyboardBuilder()
    now = tas_t()

    # If selected date is today
    if selected_date == str(now.date()):
        start_hour = max(now.hour + 1, 8)
    else:
        start_hour = 8

    for hour in range(start_hour, 19):
        kb.add(
            InlineKeyboardButton(
                text=f"{hour:02d}:00",
                callback_data=f"{selected_date} {hour:02d}:00"
            )
        )

    kb.adjust(3)
    return kb.as_markup()
