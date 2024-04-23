from aiogram.types.reply_keyboard_markup import ReplyKeyboardMarkup
from aiogram.types.keyboard_button import KeyboardButton
from locales import buttons as btn


# REPLY KEYBOARD
def main_menu():
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="👨‍🎨Про проєкт")],
            [
                KeyboardButton(text="Реквізити"),
                KeyboardButton(text="План занять")
            ],
            [KeyboardButton(text='Контакти')],
            [
                KeyboardButton(text='😉Надіслати відгук'),
                KeyboardButton(text='Надіслати заявку'),
                KeyboardButton(text='Надіслати картинку')
            ],
            [
                KeyboardButton(text='Надіслати групу фото'),
                KeyboardButton(text='Телефон', request_contact=True),
                KeyboardButton(text="Локація", request_location=True)
            ],
            [
                KeyboardButton(text='Екзотика')
            ]
        ],
        resize_keyboard=True
    )
    return kb


def sub_contacts():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Соц. мережі"), KeyboardButton(text="Телефон")],
            [KeyboardButton(text='Назад')]
        ],
        resize_keyboard=True
    )


def admin_main():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Додати адміністратора"),
             KeyboardButton(text="Видалити адміністратора")],
            [KeyboardButton(text='Розсилка')]
        ],
        resize_keyboard=True
    )


def admin_mass_sending():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Скасувати")]
        ],
        resize_keyboard=True
    )


# --- Production ---
def select_lang():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Українська🇺🇦"),
             KeyboardButton(text="English")]
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
