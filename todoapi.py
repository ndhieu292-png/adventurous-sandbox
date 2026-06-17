from flask import Flask
import json
app = Flask(__name__)
def load_list():
    with open ("todos.json", "r") as file:
        lists = json.load(file)
        if len(lists) == 0:
            return None
    print("Loaded", lists)
    return lists


def save_list(lists):
    with open ("todos.json", "w") as file:
        json.dump(lists, file)


@app.route("/todos")
def show_todo():
    lists = load_list()
    todos = []
    for item in lists:
        todos.append(item)
    return str(todos)


@app.route("/todos/add/<task>")
def add_task(task):
    lists = load_list()
    new_id = 1
    if len(lists) > 0:
        new_id = lists[-1]["id"] + 1
    todo = {"id": new_id, "task": task}
    lists.append(todo)
    save_list(lists)
    return {"message": "task added", "task": task}


@app.route("/todos/delete/<id>")
def del_task(id):
    lists = load_list()
    if lists is None:
        return {"Empty lists"}
    found = False
    for item in lists:
        if str(item["id"]) == id:
            found = True
            lists.remove(item)
            save_list(lists)
    if found == False:
        return {"Not available"}


@app.route("/todos/<id>")
def show_id(id):
    lists = load_list()
    if lists is None:
        return {"Empty lists"}
    found = False
    for item in lists:
        if str(item["id"]) == id:
            found = True
            return str(item)
    if found == False:
        return {"Not found"}


@app.route("/todos/update/<id>/<task>")
def update(id, task):
    lists = load_list()
    if lists is None:
        return {"Empty lilsts"}
    found = False
    for item in lists:
        if str(item["id"]) == id:
            found = True
            item["task"] = task
            save_list(lists)
            return {"Update succeeded"}
    if found == False:
        return {"Not found"}
    
    
app.run(debug=True)