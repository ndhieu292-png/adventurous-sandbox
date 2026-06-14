from flask import Flask
import requests

app = Flask(__name__)

def get_pokemon(name):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}")
    if response.status_code == 404:
        return None
    return response.json()


@app.route("/pokemon/<name>")
def pokemon_info(name):
    data = get_pokemon(name)
    if data is None:
        return "Pokemon not found"
    return {"name": data["name"], "height": data["height"], "weight": data["weight"]}


@app.route("/pokemon/<name>/ability")
def pokemon_ability(name):
    data = get_pokemon(name)
    if data is None:
        return "Pokemon not found"
    return {"ability": data["abilities"][0]["ability"]["name"]}


@app.route("/pokemon/<name>/type")
def pokemon_type(name):
    data = get_pokemon(name)
    if data is None:
        return "Pokemon not found"
    return {"type": data["types"][0]["type"]["name"]}
if __name__ == "__main__":
    app.run(debug=True)