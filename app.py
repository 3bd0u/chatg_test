from flask import Flask, jsonify

app = Flask(__name__)

# Route principale
@app.route("/")
def home():
    return "Hello, Flask API is running!"

# Exemple de route JSON
@app.route("/api/test", methods=["GET"])
def test_api():
    return jsonify({"message": "API test successful 🚀"})

if __name__ == "__main__":
    # debug=True : recharge automatique si tu modifies ton code
    app.run(host="0.0.0.0", port=5000, debug=True)


