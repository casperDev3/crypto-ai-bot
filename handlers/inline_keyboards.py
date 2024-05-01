from aiogram import types
from keyboards import inline, reply
from creds import main
from db import main as db

dp = main.dp


@dp.callback_query(lambda c: c.data.startswith("select_subscription_"))
async def select_subscription(callback_query: types.CallbackQuery):
    print(callback_query)
    data = callback_query.data
    cid = callback_query.from_user.id
    msg_id = callback_query.message.message_id
    subscription_id = data.split("_")[2]
    print(subscription_id)
    result = db.update_subscription(cid, subscription_id)
    if result:
        await main.bot.edit_message_text("Підписка успішно змінена", cid, msg_id)
    else:
        await main.bot.edit_message_text("Помилка", cid, msg_id)

    await main.bot.delete_message(cid, msg_id)



@dp.callback_query(lambda c: c.data)
async def courses(callback_query: types.CallbackQuery):
    data = callback_query.data
    cid = callback_query.from_user.id
    msg_id = callback_query.message.message_id
    if data == "update_subscription":
        all_payments_subscriptions = db.get_paid_subscriptions()
        txt = "Оберіть підписку:\n"
        for item in all_payments_subscriptions:
            txt += f"{item[1]} - {item[2]}\n"

        await main.bot.send_message(cid, txt, reply_markup=inline.select_subscription_type(all_payments_subscriptions))
    elif data == "cancel_subscription":
        result = db.cancel_subscription(cid)
        if result:
            await main.bot.edit_message_text("Підписка скасована", cid, msg_id)
        else:
            await main.bot.edit_message_text("Помилка", cid, msg_id)
#  select_subscription_{item[0]}- this is a callback_data for each subscription
