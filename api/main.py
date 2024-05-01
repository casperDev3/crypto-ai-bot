from quart import Quart, request, jsonify
import asyncio
from aiogram import Bot, types
from db import main as db

app = Quart(__name__)

TOKEN = "6360343069:AAGWRCbHC4RmeT8rPrzpF3HPJqMLQymx0dc"  # replace with your Telegram bot token
bot = Bot(TOKEN)


@app.route('/send', methods=['POST'])
async def send_message():
    try:
        data = await request.get_json()
        active_users = db.get_user_with_subscription()
        print(active_users)
        count_success = 0
        count_failed = 0
        count_total = 0
        with open("../db/last_signal.json", "w") as f:
            f.write(str(data))
        if active_users:
            for user_id in active_users:
                try:
                    locale = db.get_current_lang(user_id)
                    if locale == "uk":
                        message_data = data['data']
                    else:
                        message_data = data['data']['locales'][locale]

                    message = message_data['message']
                    media_urls = message_data['media']

                    # Dispatch to background
                    await asyncio.create_task(send_async_message(user_id, message, media_urls))
                    count_success += 1
                    continue
                except Exception as e:
                    app.logger.error(f"Error during sending message: {e}")
                    count_failed += 1
                    continue
                finally:
                    count_total += 1

            return jsonify({"success": True, "message": "Message and media are being sent", "data": {
                "total_msg": count_total,
                "success_msg": count_success,
                "failed_msg": count_failed
            }}), 202
        else:
            return jsonify({"success": False, "message": "No users found with subscribtion"}), 202
    except Exception as e:
        app.logger.error(f"Error during sending message: {e}")
        return jsonify({"success": False, "message": "Error during sending message"}), 500


async def send_async_message(cid, message, media_urls):
    await bot.send_message(cid, message, protect_content=True)
    media_group = [types.InputMediaPhoto(media=url) for url in media_urls]
    await bot.send_media_group(cid, media=media_group)


if __name__ == '__main__':
    app.run()
