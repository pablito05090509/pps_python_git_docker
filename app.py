from flask import Flask, jsonify
from bayeta import frotar

app = Flask(__name__)

@app.route("/")
def home():
    return "Hola, mundo"

@app.route("/frotar/<int:n>")
def frotar_endpoint(n):
    return jsonify(frotar(n))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
