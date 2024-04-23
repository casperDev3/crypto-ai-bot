from creds import main as c
import json


def create_new_user(user_data):
    with open("db/users.json", "r") as file:
        users = json.load(file)

    for user in users:
        if user["chat_id"] == user_data["chat_id"]:
            return

    users.append(user_data)

    with open("db/users.json", "w") as f:
        json.dump(users, f)


def update_locale_user(chat_id, locale):
    with open("db/users.json", "r") as file:
        users = json.load(file)

    for u in users:
        if u["chat_id"] == chat_id:
            u["locale"] = locale

    with open("db/users.json", "w") as f:
        json.dump(users, f)


def get_current_lang(chat_id):
    with open("db/users.json", "r") as file:
        users = json.load(file)

    for u in users:
        if u["chat_id"] == chat_id:
            return u["locale"]
