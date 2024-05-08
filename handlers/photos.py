from aiogram.types import Message
from creds import main

dp = main.dp


@dp.message(lambda msg: msg.photo)
async def get_media_from_user(msg: Message):
    photo = msg.photo[-1]
    file_id = photo.file_id
    file = await main.bot.get_file(file_id)
    file_path = file.file_path

    await main.bot.download(file=file, destination=f"assets/downloads/photo_{file_id}.jpg")
    await msg.answer("Success!")
