import json


FILE_PATH = "data/users.json"


def save_user(user):
    try:
        with open(FILE_PATH, "r") as file:
            users = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        users = []

    users.append({
        "name": user.name,
        "email": user.email,
        "password": user.password
    })

    with open(FILE_PATH, "w") as file:
        json.dump(users, file, indent=4)


def get_users():
    try:
        with open(FILE_PATH, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []