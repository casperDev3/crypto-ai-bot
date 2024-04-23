from aiogram.types.inline_keyboard_markup import InlineKeyboardMarkup
from aiogram.types.inline_keyboard_button import InlineKeyboardButton


def plan_menu():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Python Core", callback_data="plan_python_core")],
            [InlineKeyboardButton(text="HTML & CSS", callback_data="plan_html_css")],
            [InlineKeyboardButton(text="NEXT.js 14", callback_data="plan_next14"),
             InlineKeyboardButton(text="Контакти", callback_data="plan_contacts")]
        ]
    )
