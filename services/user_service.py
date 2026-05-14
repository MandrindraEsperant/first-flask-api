users = []

def get_all_users():
    return users

def create_user(data):
    user = {
        "id": len(users) + 1,
        "name": data.get("name"),
        "email": data.get("email")
    }
    users.append(user)
    return user