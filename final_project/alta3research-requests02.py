import json
import pprint
import requests

from flask import Flask
from flask import redirect
from flask import request
from flask import jsonify

poke_data = {"name": "Arceus", "type": "Normal", "level": 100}

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        data = request.json
        if data:
            data= json.loads(data)
            name = data["name"]
            typ = data["type"]
            lvl = data["level"]
            poke_data.append({"name": name, "type": typ, "level": lvl})
    
    
    poke_data = jsonify(poke_data)

    resp = requests.post(__name__, json=poke_data)
    return pprint(resp.json())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
# URL= "http://127.0.0.1:2224/"

# resp= requests.get(URL).json()

# pprint(resp)