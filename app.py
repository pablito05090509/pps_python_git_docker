from flask import Flask, jsonify, request
from bayeta import frotar, agregar_frases

app = Flask(__name__)

@app.route("/")
def index():
    return "¡Bienvenido a la Bayeta de la Fortuna!"

@app.route("/frotar/<int:n_frases>")
def get_frases(n_frases):
    frases = frotar(n_frases)
    return jsonify(frases)

@app.route("/frotar/add", methods=["POST"])
def add_frases():
    data = request.get_json()
    if not data or "frases" not in data:
        return jsonify({"error": "Debes enviar un JSON con la clave 'frases'"}), 400
    
    nuevas = data["frases"]
    if not isinstance(nuevas, list) or not all(isinstance(f, str) for f in nuevas):
        return jsonify({"error": "La clave 'frases' debe ser una lista de strings"}), 400

    count = agregar_frases(nuevas)
    return jsonify({"insertadas": count}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
