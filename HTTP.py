from flask import Flask, request

app = Flask(__name__)

users = []

@app.route("/add/<name>")
def add_user(name):

    users.append(name)

    return str(users)


@app.route("/info", methods=["POST"])
def add_info():

    info = []

    info.append(request.args.get("name"))
    info.append(request.method)
    info.append(request.path)

    return str(info)


@app.route("/change/<int:amount>", methods=["POST"])
def change_qty(amount):

    quantity = int(request.form.get("quantity"))

    return str(quantity + amount)

app.run(debug=True)