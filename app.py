from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load Crop Model & Label Encoder
crop_model = pickle.load(open("models/crop_model.pkl", "rb"))
crop_label_encoder = pickle.load(open("models/crop_label_encoder.pkl", "rb"))

# Load Fertilizer Model, Scaler & Label Encoders
fertilizer_model = pickle.load(open("models/fertilizer_model.pkl", "rb"))
scaler = pickle.load(open("models/scaler.pkl", "rb"))
fertilizer_label_encoder = pickle.load(open("models/fertilizer_label_encoder.pkl", "rb"))
fertilizer_name_encoder = pickle.load(open("models/fertilizer_name_encoder.pkl", "rb"))


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/crop")
def crop_page():
    return render_template("crop.html")


@app.route("/fertilizer")
def fertilizer_page():
    return render_template("fertilizer.html")


@app.route("/predict_crop", methods=["POST"])
def predict_crop():
    try:
        # Get user inputs
        N = float(request.form["N"])
        P = float(request.form["P"])
        K = float(request.form["K"])
        temperature = float(request.form["temperature"])
        humidity = float(request.form["humidity"])
        ph = float(request.form["ph"])
        rainfall = float(request.form["rainfall"])

        # Convert input to NumPy array
        input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])

        # Predict using model
        crop_prediction = crop_model.predict(input_data)
        crop_name = crop_label_encoder.inverse_transform([crop_prediction[0]])[0]

        return render_template("result.html", prediction=crop_name, model_type="Crop Recommendation")

    except Exception as e:
        return f"Error: {e}"


@app.route("/predict_fertilizer", methods=["POST"])
def predict_fertilizer():
    try:
        # Get user inputs
        soil_type = int(request.form["soil_type"])
        crop_type = int(request.form["crop_type"])
        nitrogen = float(request.form["nitrogen"])
        phosphorus = float(request.form["phosphorus"])
        potassium = float(request.form["potassium"])
        temperature = float(request.form["temperature"])
        humidity = float(request.form["humidity"])
        moisture = float(request.form["moisture"])

        # Create input array
        input_data = np.array([[soil_type, crop_type, nitrogen, phosphorus, potassium, temperature, humidity, moisture]])

        # Scale input data
        input_data_scaled = scaler.transform(input_data)

        # Predict using model
        fertilizer_prediction = fertilizer_model.predict(input_data_scaled)
        fertilizer_name = fertilizer_name_encoder.inverse_transform([fertilizer_prediction[0]])[0]

        return render_template("result.html", prediction=fertilizer_name, model_type="Fertilizer Recommendation")

    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
    app.run(debug=True)
