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


def update_subscription():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Змінити", callback_data="update_subscription"),
             InlineKeyboardButton(text="Скасувати", callback_data="cancel_subscription")]
        ]
    )


def select_subscription_type(types: list):
    buttons = []
    for item in types:
        buttons.append([InlineKeyboardButton(text=item[1], callback_data=f"select_subscription_{item[0]}")])
    return InlineKeyboardMarkup(inline_keyboard=buttons)
