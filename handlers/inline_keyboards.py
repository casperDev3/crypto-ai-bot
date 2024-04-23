from aiogram import types
from keyboards import inline, reply
from creds import main

dp = main.dp


@dp.callback_query(lambda c: c.data)
async def courses(callback_query: types.CallbackQuery):
    data = callback_query.data
    cid = callback_query.from_user.id
    msg_id = callback_query.message.message_id
    if data == "plan_python_core":
        # await main.bot.send_message(cid, "Program Python: ")
        await main.bot.edit_message_text(
            text="Program Python: https://drohobych.itstep.org/",
            chat_id=cid,
            message_id=msg_id,
            reply_markup=inline.plan_menu(),
            disable_web_page_preview=True
        )
    elif data == "plan_html_css":
        await main.bot.edit_message_text(
            text="HTML Program: https://drohobych.itstep.org/",
            chat_id=cid,
            message_id=msg_id,
            reply_markup=inline.plan_menu(),
            disable_web_page_preview=True
        )
    elif data == "plan_next14":
        await main.bot.edit_message_text(
            text="NEXT.js 14 Program: https://drohobych.itstep.org/",
            chat_id=cid,
            message_id=msg_id,
            reply_markup=inline.plan_menu(),
            disable_web_page_preview=True
        )
    elif data == "plan_contacts":
        await main.bot.delete_message(chat_id=cid, message_id=msg_id)
        await main.bot.send_message(cid, "Ви відкрили підменю контакти", reply_markup=reply.sub_contacts())
