from creds import main as c
import json

cursor = c.cursor


def create_new_user(user_data):
    cursor.execute("SELECT * FROM users WHERE chat_id = %s", (user_data["chat_id"],))
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO users (chat_id, first_name, last_name, username, locale, package_id) VALUES (%s, "
                       "%s, %s, %s, %s, %s)",
                       (user_data["chat_id"], user_data["first_name"], user_data["last_name"], user_data["username"],
                        user_data["locale"], 1))

    c.conn.commit()


def update_locale_user(chat_id, locale):
    cursor.execute("UPDATE users SET locale = %s WHERE chat_id = %s", (locale, chat_id))
    c.conn.commit()


def get_current_lang(chat_id):
    cursor.execute("SELECT locale FROM users WHERE chat_id = %s", (chat_id,))
    result = cursor.fetchone()
    if result is not None:
        print("Answer from db", result[0])
        return result[0]
    else:
        print("No data found for chat_id", chat_id)
        return None


def update_phone_number(chat_id, phone_number):
    cursor.execute("UPDATE users SET phone_number = %s WHERE chat_id = %s", (phone_number, chat_id))
    c.conn.commit()
