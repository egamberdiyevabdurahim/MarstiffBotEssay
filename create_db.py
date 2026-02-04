import asyncio

from database_config.config import ADMINISTRATION_GROUP_ID
from loader import (
    bot,
    User, History, Errors, Balance, Transaction,
    Essentials, TGGroup, TGGroupSection, Event, EventUser, Essay, EssayUser,
)


async def create_tables():
    tables = [
        User, History, Errors, Balance, Transaction,
        Essentials, TGGroup, TGGroupSection, Event, EventUser,
        Essay, EssayUser,
    ]
    for table in tables:
        await table.create_table()


async def add_items():
    await Essentials.create(
        key="credit_card",
        val="5614 6822 1973 4029"
    )

    await Essay.create(
        video="BAACAgQAAxkBAAMraYKDh5AKzdexP1C7VztpKvStghsAAhMKAALhTh1QrEkjgmOstgY4BA",
        cost=100000.00,
        section=31
    )


async def create_group_sections():
    await TGGroup.create(
        group_id=ADMINISTRATION_GROUP_ID,
        status=1
    )
    gr = await TGGroup.get_by_chat_id(chat_id=ADMINISTRATION_GROUP_ID)
    idn = await bot.create_forum_topic(
        chat_id=gr.group_id,
        name="Notifications",
    )
    await TGGroupSection.create(
        group_idn=gr.idn,
        section_id=idn.message_thread_id,
        type_connected=0,
        status=1,
    )

    idn = await bot.create_forum_topic(
        chat_id=ADMINISTRATION_GROUP_ID,
        name="New comers",
    )
    await TGGroupSection.create(
        group_idn=gr.idn,
        section_id=idn.message_thread_id,
        type_connected=1,
        status=1,
    )

    idn = await bot.create_forum_topic(
        chat_id=ADMINISTRATION_GROUP_ID,
        name="Succeed payments",
    )
    await TGGroupSection.create(
        group_idn=gr.idn,
        section_id=idn.message_thread_id,
        type_connected=2,
        status=1,
    )

    idn = await bot.create_forum_topic(
        chat_id=ADMINISTRATION_GROUP_ID,
        name="Failed payments",
    )
    await TGGroupSection.create(
        group_idn=gr.idn,
        section_id=idn.message_thread_id,
        type_connected=3,
        status=1,
    )

    idn = await bot.create_forum_topic(
        chat_id=ADMINISTRATION_GROUP_ID,
        name="Payment history",
    )
    await TGGroupSection.create(
        group_idn=gr.idn,
        section_id=idn.message_thread_id,
        type_connected=4,
        status=1,
    )


async def runner_create_tb():
    await create_tables()
    await add_items()
    await create_group_sections()


asyncio.run(runner_create_tb())
