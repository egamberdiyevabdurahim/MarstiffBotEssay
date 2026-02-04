from aiogram.types import Message, CallbackQuery

from loader import Errors, User, History


async def error_logger(u_idn=None, description=None, error_pl=None, u=None):
    u = u or await User.get_data(u_idn)
    if u:
        await Errors.create(
            u_idn=u.idn,
            description=description,
            error_pl=error_pl
        )
    return None


async def logger(obj: Message | CallbackQuery, u, mess):
    chat_id = u.id
    try:
        u = await User.get_data(chat_id)
        if u:
            await History.create(
                u_idn=u.idn,
                message=obj.text if mess else obj.data,
                message_id=obj.message_id if mess else obj.message.message_id
            )
            await u.use()
        return True

    except Exception as e:
        await error_logger(u_idn=chat_id, description=e, error_pl="activity_maker")
        return None
