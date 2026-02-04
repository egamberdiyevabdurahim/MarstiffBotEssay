import asyncio
import schedule

from aiogram import types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from views.admin import (
    accept_decline_payment_hl, main_hl as main_hl_admin, event_mgmt_hl,
)
from views.user import (
    login_hl, main_hl as main_hl_user, book_essay_lesson_hl, participate_in_an_event_hl,
)
from main import router

from utils.database_dumper import dump_and_send

from loader import bot, dp


@dp.message(Command('support', 'help'))
async def support_command(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer(f"For help: @✅")


async def schedule_task_for_inactivate():
    while True:
        schedule.run_pending()
        await asyncio.sleep(1)


async def main():
    dp.include_routers(
        router,

        # ADMIN
        accept_decline_payment_hl.router,
        main_hl_admin.router,
        event_mgmt_hl.router,

        # USER
        login_hl.router,
        main_hl_user.router,
        book_essay_lesson_hl.router,
        participate_in_an_event_hl.router,
    )
    # dp.update.outer_middleware(middleware=ErrorLoggingMiddleware())
    await dp.start_polling(bot)

async def init():
    schedule.every().day.at("19:00").do(lambda: asyncio.create_task(dump_and_send()))
    await asyncio.gather(main(), schedule_task_for_inactivate())

if __name__ == '__main__':
    try:
        asyncio.run(init())
    except Exception as e:
        print(e)
