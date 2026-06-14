from flask import Flask
import json
app = Flask(__name__)
def load_users():
    with open("users.json", "r") as file:
        return json.load(file)
def save_users(data):
    with open("users.json", "w") as file:
        json.dump(data, file, indent=4)
@app.route("/users")
def get_users():
    return load_users()
@app.route("/add/<name>")
def add_user(name):
    users = load_users()
    new_id = 1
    if len(users) > 0:
        new_id = users[-1]["id"] + 1
    user = {"id": new_id, "name": name}
    users.append(user)
    save_users(users)
    return {"message": "user added", "user": user}
@app.route("/delete/<id>")
def delete_user(id):
    users = load_users()
    for user in users:
        if str(user["id"]) == id:
            users.remove(user)
            save_users(users)
            return {"message": "user deleted", "user": user}
    return {"error": "user not found"}
if __name__ == "__main__":
    app.run(debug=True)