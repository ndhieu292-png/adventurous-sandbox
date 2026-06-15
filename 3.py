from flask import Flask
import requests
app = Flask(__name__)

def get_pokemon(name):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}")
    if response.status_code == 404:
        return None
    return response.json()

@app.route("/pokemon/<name>")
def information(name):
    data = get_pokemon(name)
    if data is None:
        return {"error": "Pokemon not found"}
    return {"name": data["name"], "height": data["height"], "weight": data["weight"]}

@app.route("/pokemon/<name>/types")
def type_pokemon(name):
    data = get_pokemon(name)
    if data is None:
        return {"error": "Pokemon not found"}
    types = []
    for pokemon_type in data["types"]:
        types.append(pokemon_type["type"]["name"])
    return types

@app.route("/pokemon/<name>/abilities")
def ability_pokemon(name):
    data = get_pokemon(name)
    if data is None:
        return {"error": "Pokemon not found"}
    abilities = []
    for ability in data["abilities"]:
        abilities.append(ability["ability"]["name"])
    return abilities

@app.route("/pokemon/<name>/summary")
def summary_pokemon(name):
    data = get_pokemon(name)
    if data is None:
        return {"error": "Pokemon not found"}
    types = []
    for pokemon_type in data["types"]:
        types.append(pokemon_type["type"]["name"])
    abilities = []
    for ability in data["abilities"]:
        abilities.append(ability["ability"]["name"])
    return {"name": data["name"], "height": data["height"], "weight": data["weight"], "types": types, "abilities": abilities}

if __name__ == "__main__":
    app.run(debug=True)