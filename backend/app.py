from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import pandas as pd
import joblib
app = Flask(__name__, static_folder="../frontend")
CORS(app)
model = joblib.load("house_model.joblib")
@app.route("/")
def home():
    return send_from_directory(app.static_folder, "index.html")
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    input_data = pd.DataFrame({
        "living area": [data["living_area"]],
        "Number of Rooms": [data["number_of_rooms"]],
        "Postal Code": [data["postal_code"]]
    })

    prediction = model.predict(input_data)

    return jsonify({
        "Predicted Price": float(prediction[0])
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)