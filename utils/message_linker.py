

async def message_linker(mess):
    chat_id = mess.chat.id
    message_id = mess.message_id

    # Remove -100 prefix if exists
    internal_id = str(chat_id).replace("-100", "")

    message_link = f"https://t.me/c/{internal_id}/{message_id}"
    return message_link