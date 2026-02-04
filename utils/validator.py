import aiogram.types
from aiogram.types import Message, CallbackQuery

from loader import User
from utils.logger import logger, error_logger
from utils.message_deleter import message_deleter


async def vld(
        o: Message | CallbackQuery = None,
        u: aiogram.types.User = None,
        ans: bool = True,
        ans_mg: str = None,
        ans_url: str = None,
        show_alert: bool = None,
        delete: bool = None,
        delete_ex: bool = None,
        delete_ex_ex: bool = None,
        r_u: bool = True
):
    u_id = u.id
    try:
        o_mess = True if isinstance(o, Message) else False
        await logger(obj=o, u=u, mess=o_mess)

        if ans and not o_mess:
            await o.answer(text=ans_mg, show_alert=show_alert, url=ans_url)

        if delete:
            if o_mess:
                await message_deleter(u_id=u_id, message_id=o.message_id)

            else:
                await message_deleter(u_id=u_id, message_id=o.message.message_id)

        if delete_ex:
            if o_mess:
                await message_deleter(u_id=u_id, message_id=o.message_id-1)

            else:
                await message_deleter(u_id=u_id, message_id=o.message.message_id - 1)

        if delete_ex_ex:
            if o_mess:
                await message_deleter(u_id=u_id, message_id=o.message_id - 2)

            else:
                await message_deleter(u_id=u_id, message_id=o.message.message_id - 2)

        if r_u:
            user = await User.get_data(chat_id=u.id)
            return user
        return None

    except Exception as e:
        await error_logger(u_idn=u_id, description=e, error_pl="validator")
        return None