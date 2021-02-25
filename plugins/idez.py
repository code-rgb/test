from pyrogram.errors import BadRequest
from userge import userge, Message


@userge.on_cmd(
    "idez",
    about={
        "header": "Deezer but yeah inline",
        "usage": "{tr}idez [text]",
    },
)
async def ideez_(message: Message):
    reply = message.reply_to_message
    reply_id = reply.message_id if reply else None
    if message.input_str:
        input_query = message.input_str
    elif reply:
        if reply.text:
            input_query = reply.text
        elif reply.caption:
            input_query = reply.caption
    if not input_query:
        return await message.err("Input Not Found", del_in=5)

    x = await userge.get_inline_bot_results(
            "@DeezerMusicBot", input_query
    )
    try:
        await message.delete()
        await userge.send_inline_bot_result(
            chat_id=message.chat.id,
            query_id=x.query_id,
            result_id=x.results[0].id,
            reply_to_message_id=reply_id
        )
    except (IndexError, BadRequest):
        await message.err("song not found", del_in=5)