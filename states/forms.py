import json

from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from creds import main
from keyboards import reply
from auth import main as auth
from utils import mass_sending as send
from locales import messages
from db import main as db

dp = main.dp


class RegistrationStates(StatesGroup):
    wait_for_number = State()


@dp.message(RegistrationStates.wait_for_number)
async def get_user_number(msg: types.Message, state: FSMContext):
    locale = db.get_current_lang(msg.from_user.id)
    if msg.text == "Назад⬅️" or msg.text == "Back⬅️":
        await state.clear()
        await msg.answer(messages.cancel_registration[locale], reply_markup=reply.start_auth(locale))
    else:
        db.update_phone_number(msg.from_user.id, msg.text)
        await state.clear()
        await msg.answer(messages.success_registration[locale], reply_markup=reply.gen_menu())
