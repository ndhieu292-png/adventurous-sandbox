import json
def load_users():
    with open("users.json", "r") as file:
        users = json.load(file)
    print("Loaded:", users)
    return users
def dump_users(users):
    with open("users.json", "w") as file:
        json.dump(users, file)
users = load_users()
while True:
    user = input("Enter name, q for quit: ")
    if user == "q":
        break
    users.append(user)
dump_users(users)