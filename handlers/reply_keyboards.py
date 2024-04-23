from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove, FSInputFile
from aiogram.utils.media_group import MediaGroupBuilder

from keyboards import inline, reply
from creds import main
from states import forms
from auth import main as auth
from db import main as db
from locales import messages as msg

dp = main.dp


@dp.message()
async def special_msg(message: types.Message, state: FSMContext) -> None:
    cid = message.chat.id
    content = message.text

    # --- Production ---English🏴󠁧󠁢󠁥󠁮󠁧󠁿󠁿
    if content == "Українська🇺🇦":
        db.update_locale_user(cid, 'uk')
        await message.answer(msg.txt_after_select_lang['uk'],
                             reply_markup=reply.start_auth('uk'))
    elif content == "English":
        db.update_locale_user(cid, 'en')
        await message.answer(msg.txt_after_select_lang['en'],
                             reply_markup=reply.start_auth('en'))

    elif content == "Реєстрація" or content == "Registration":
        locale = db.get_current_lang(cid)
        await message.answer("Тут потрібно уточнити, щодо авторизації та реєстрації",
                             reply_markup=reply.gen_menu())

    elif content == "Авторизація" or content == "Authorization":
        await message.answer("Тут потрібно уточнити, щодо авторизації та реєстрації",
                             reply_markup=reply.gen_menu())
