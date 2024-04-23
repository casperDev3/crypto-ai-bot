import json

from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from creds import main
from keyboards import reply
from auth import main as auth
from utils import mass_sending as send

dp = main.dp


class RegistrationStates(StatesGroup):
    wait_for_feedback = State()


class RequestForm(StatesGroup):
    wait_for_name = State()
    wait_for_email = State()
    wait_for_comment = State()


class AddNewAdmin(StatesGroup):
    wait_for_admin_id = State()


class MassSending(StatesGroup):
    wait_for_content_msg = State()


@dp.message(MassSending.wait_for_content_msg)
async def get_new_admin_id(msg: types.Message, state: FSMContext):
    if msg.text == "Скасувати":
        await state.clear()
        await msg.answer("Ви відмінили розсилку!", reply_markup=reply.admin_main())
    else:
        await send.global_mass_sending(msg.text, msg.from_user.id)
        await state.clear()


@dp.message(AddNewAdmin.wait_for_admin_id)
async def get_new_admin_id(msg: types.Message, state: FSMContext):
    auth.add_new_admin(int(msg.text))
    await state.clear()
    await msg.answer("Адміна успішно додано!", reply_markup=reply.admin_main())


@dp.message(RegistrationStates.wait_for_feedback)
async def get_user_feedback(msg: types.Message, state: FSMContext):
    print("Requests", msg.text)
    await state.clear()


@dp.message(RequestForm.wait_for_name)
async def get_name_req_form(msg: types.Message, state: FSMContext):
    await state.update_data(name=msg.text)
    await msg.answer("Введіть вашу пошту: ")
    await state.set_state(RequestForm.wait_for_email)


@dp.message(RequestForm.wait_for_email)
async def get_email_req_form(msg: types.Message, state: FSMContext):
    await state.update_data(email=msg.text)
    await msg.answer("Введіть ваш коментар: ")
    await state.set_state(RequestForm.wait_for_comment)


@dp.message(RequestForm.wait_for_comment)
async def get_comment_req_form(msg: types.Message, state: FSMContext):
    await state.update_data(comment=msg.text)
    with open("data/requests.json", "r", encoding="utf-8") as file:
        all_req = json.load(file)
        req_data = await state.get_data()
        all_req.append(req_data)
    with open("data/requests.json", "w", encoding="utf-8") as f:
        json.dump(all_req, f)

    await state.clear()
    await msg.answer("Дякуємо! Ваша заявка на розгляді", reply_markup=reply.main_menu())
