from aiogram.types import ReplyKeyboardRemove


async def reply_keyboard_rm(mess):
    m = await mess.answer(text=".", reply_markup=ReplyKeyboardRemove())
    await m.delete()
