from aiogram import types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from creds import main
from keyboards import reply
from auth import main as auth
from db import main as db

dp = main.dp


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    db.create_new_user({
        "chat_id": message.from_user.id,
        "first_name": message.from_user.first_name,
        "last_name": message.from_user.last_name,
        "locale": "uk",
        "username": message.from_user.username
    })
    txt = f"""Привіт, {message.from_user.first_name}. Оберіть мову в боті / Select a language in the bot"""
    await message.answer(txt, reply_markup=reply.select_lang())


@dp.message(Command("poll"))
async def poll(msg: types.Message):
    cid = msg.from_user.id
    await main.bot.send_poll(
        chat_id=cid,
        question="Test Question",
        options=["One", "Two"],
        type="regular",
        is_anonymous=False,
        allows_multiple_answers=True
    )


@dp.message(Command("admin"))
async def welcome_admin(msg: types.Message):
    if auth.is_admin(msg.from_user.id):
        await msg.answer("Вітає вам у режимі адміністратора", reply_markup=reply.admin_main())
    else:
        await msg.answer("You haven't access!", reply_markup=reply.main_menu())
