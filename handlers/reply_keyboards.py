import json

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
    locale = db.get_current_lang(cid)

    # --- Production ---
    if content == "Українська🇺🇦":
        db.update_locale_user(cid, 'uk')
        await message.answer(msg.txt_after_select_lang['uk'],
                             reply_markup=reply.start_auth('uk'))
    elif content == "English🏴󠁧󠁢󠁥󠁮󠁧󠁿":
        db.update_locale_user(cid, 'en')
        await message.answer(msg.txt_after_select_lang['en'],
                             reply_markup=reply.start_auth('en'))

    elif content == "Реєстрація🏛" or content == "Registration🏛":
        await state.set_state(forms.RegistrationStates.wait_for_number)
        await message.answer(msg.txt_reg[locale],
                             reply_markup=reply.reg_menu(locale))

    elif content == "Авторизація👤" or content == "Authorization👤":
        await message.answer("Тут потрібно уточнити, щодо авторизації та реєстрації",
                             reply_markup=reply.gen_menu())

    elif content == "Підписки" or content == "Subscriptions":
        subscriptions_type = db.get_subscriptions(cid)
        print(subscriptions_type)
        await message.answer(f"Ваша підписка: {subscriptions_type[1]}",
                             reply_markup=inline.update_subscription())

    elif content == "Сигнали" or content == "Signals":
        try:
            with open("db/last_signal.json", "r") as f:

                # {'data': {'message': 'Тестове повідомлення', 'media': ['https://cdn.pixabay.com/photo/2016/05/05/02/37/sunset-1373171_1280.jpg', 'https://cdn.pixabay.com/photo/2016/05/05/02/37/sunset-1373171_1280.jpg'], 'locales': {'en': {'message': 'Test messsage', 'media': ['https://cdn.pixabay.com/photo/2016/05/05/02/37/sunset-1373171_1280.jpg', 'https://cdn.pixabay.com/photo/2016/05/05/02/37/sunset-1373171_1280.jpg', 'https://cdn.pixabay.com/photo/2016/05/05/02/37/sunset-1373171_1280.jpg', 'https://cdn.pixabay.com/photo/2016/05/05/02/37/sunset-1373171_1280.jpg']}}}}
                last_signal = json.loads(f)
                print(last_signal)
                message = last_signal['data']['message']
                media = last_signal['data']['media']
                user_locale = db.get_current_lang(cid)
                if user_locale == "uk":
                    text = message
                    media_urls = media
                else:
                    text = last_signal['data']['locales'][user_locale]['message']
                    media_urls = last_signal['data']['locales'][user_locale]['media']

                await message.answer(text)
                media_group = [types.InputMediaPhoto(media=url) for url in media_urls]
        except Exception as e:
            print(e)
            await message.answer("Помилка під час відправлення сигналу, зверніться до адміністратора")
    elif content == "Про нас" or content == "About us":
        await message.answer("Потрібно вписати тест про нас", reply_markup=reply.gen_menu())

    elif content == "Підтримка" or content == "Support":
        await message.answer("Потрібно вписати тест підтримки", reply_markup=reply.gen_menu())