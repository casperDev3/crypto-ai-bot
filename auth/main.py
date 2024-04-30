import json


def is_admin(cid):
    with open("db/admins.json", "r") as file:
        admin_ids = json.load(file)
        if cid in admin_ids:
            return True
        return False


def add_new_admin(cid):
    with open("db/admins.json", "r") as file:
        admin_ids = json.load(file)
        admin_ids.append(cid)

    with open("db/admins.json", "w") as file:
        json.dump(admin_ids, file)
