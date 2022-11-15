from flask import Flask, jsonify, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

text = {
    "texto": ""
}


@app.route("/")
def getText():
    return jsonify(text), 200


@app.route("/", methods=["POST"])
def createText():
    dict_text = request.json
    text.update({"texto": dict_text["texto"]})
    return dict_text, 200


if __name__ == "__main__":
    app.run(host="localhost", port=5002, debug=True)
