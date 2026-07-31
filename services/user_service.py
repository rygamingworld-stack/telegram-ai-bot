import json
import os

FILE_PATH = "data/users.json"


def load_users():
    if not os.path.exists(FILE_PATH):
        return {}

    with open(FILE_PATH, "r") as file:
        try:
            return json.load(file)
        except:
            return {}


def save_users(users):
    with open(FILE_PATH, "w") as file:
        json.dump(users, file, indent=4)


def is_new_user(user_id):
    users = load_users()

    user_id = str(user_id)

    if user_id in users:
        return False

    users[user_id] = True

    save_users(users)

    return True