from flask import Flask, request, jsonify
import requests
from creds import main

app = Flask(__name__)


@app.route('/send', methods=['POST'])
async def send_message():
    message = request.json.get('message')
    chat_id = request.json.get('chat_id')  # Optionally pass the chat_id dynamically
    media = request.json.get('media')
    print("Message:", message, "Chat ID:", chat_id)
    await main.bot.send_message(chat_id, message, protect_content=True)
    await main.bot.send_photo(chat_id, photo=media, protect_content=True)

    return jsonify({"status": "success", "message": "Message received"}), 200


if __name__ == '__main__':
    app.run()
