import datetime
from creds import main

from aiogram.types import Message

dp = main.dp


@dp.message(lambda msg: msg.document)
async def get_file_from_user(msg: Message):
    print(msg.document)
    file = await main.bot.get_file(msg.document.file_id)
    infinity_time = int(round(datetime.datetime.timestamp(datetime.datetime.now())))
    await main.bot.download_file(file.file_path,
                                 f"assets/downloads/d_{infinity_time}_{msg.document.file_name}")
    await msg.answer("Success! Documents")
