from aiogram.types.reply_keyboard_markup import ReplyKeyboardMarkup
from aiogram.types.keyboard_button import KeyboardButton
from locales import buttons as btn


# --- Production ---
def select_lang():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Українська🇺🇦"),
             KeyboardButton(text="English🏴󠁧󠁢󠁥󠁮󠁧󠁿")]
        ],
        resize_keyboard=True
    )


def start_auth(locale):
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=f"{btn.auth[f'{locale}']['reg']}"),
             KeyboardButton(text=f"{btn.auth[f'{locale}']['auth']}")]
        ],
        resize_keyboard=True
    )


def gen_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Підписки"),
             KeyboardButton(text="Сигнали")],
            [KeyboardButton(text="Про нас")]
        ],
        resize_keyboard=True
    )


def reg_menu(locale):
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=f"{btn.auth[f'{locale}']['back']}")]
        ],
        resize_keyboard=True
    )
