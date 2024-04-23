from aiogram import types
from creds import main

dp = main.dp


@dp.poll_answer()
async def poll_response(pa: types.PollAnswer):
    print(pa)
