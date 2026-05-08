from flask import Flask, jsonify
import joblib
from sklearn.datasets import load_digits
from attacks.fgsm import add_noise
from detection.detector import detect_attack
from security.validation import validate_input
import os

app = Flask(__name__)

# Load model safely
if not os.path.exists("model.pkl"):
    print("Error: model.pkl not found. Train the model first.")
    exit()

model = joblib.load("model.pkl")


@app.route("/")
def home():
    return jsonify({
        "Message": "SSDD Project Running Successfully",
        "Status": "Secure Detection System Active"
    })


@app.route("/test")
def test_attack():

    # Load sample data
    data = load_digits()
    sample = data.data[0]

    # Validate input
    if not validate_input(sample):
        return jsonify({
            "Error": "Invalid Input"
        })

    # Apply attack
    attacked = add_noise(sample)

    # Detect attack
    result = detect_attack(attacked)

    return jsonify({
        "Attack Applied": "FGSM Noise",
        "Detection Result": str(result),
        "Input": "Sample Digit Data"
    })


if __name__ == "__main__":
    app.run(debug=True)