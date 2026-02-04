from asyncio import sleep
from aiogram import Bot

from database_config.config import DEVELOPER_ID, GROUP_ID, SECOND_GROUP_ID, TOKEN
from loader import TGGroup, TGGroupSection
from utils.additions import tas_t

bot = Bot(token=TOKEN)


async def notice_developer(message, count: int = 1):
    try:
        await bot.send_message(
            text=f"#error {tas_t().strftime('%Y-%m-%d %H:%M-%S')}:\n{message}",
            chat_id=DEVELOPER_ID,
        )
    except Exception:
        if count < 16:
            await sleep(2**count)  # Exponential backoff
            await notice_developer(message, count + 1)


async def notice_admin(message, chat_id, count: int = 1):
    try:
        await bot.send_message(
            text=f"#warning:\n{message}",
            chat_id=chat_id,
        )
    except Exception as e:
        if count < 16:
            await sleep(2**count)  # Exponential backoff
            await notice_admin(message, count + 1)

        else:
            await notice_developer(message=e)


async def notice_main_group(message, section, section_data=None, effect=None, count: int = 1):
    if not section_data:
        data = await TGGroup.get_by_chat_id(chat_id=GROUP_ID)
        if data:
            section_data = await TGGroupSection.get_data_by_type_connected_group(
                group_idn=data.idn,
                type_connected=section
            )
    try:
        mess = await bot.send_message(
            text=message,
            chat_id=GROUP_ID,
            message_thread_id=section_data.section_id,
            # message_effect_id=effect,
            parse_mode="HTML"
        )
        return mess

    except Exception as e:
        if count < 6:
            await sleep(2**count)  # Exponential backoff
            await notice_main_group(
                message=message,
                section=section,
                section_data=section_data,
                effect=effect,
                count=count + 1
            )

        else:
            await notice_developer(message=e)


async def notice_second_group(message, count: int = 1):
    try:
        await bot.send_message(
            text=message,
            chat_id=SECOND_GROUP_ID,
            parse_mode="HTML"
        )
    except Exception as e:
        if count < 6:
            await sleep(2**count)  # Exponential backoff
            await notice_second_group(message, count + 1)

        else:
            await notice_developer(message=e)
