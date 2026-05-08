from flask import Flask, jsonify, request
import joblib
import os

from attacks.fgsm import add_noise
from detection.detector import detect_attack
from security.validation import validate_input
from sklearn.datasets import load_digits

app = Flask(__name__)

# -----------------------------
# Load ML Model Safely
# -----------------------------
MODEL_PATH = "model.pkl"

if os.path.exists(MODEL_PATH):
    model = joblib.load(MODEL_PATH)
else:
    model = None
    print("⚠ Warning: model.pkl not found (ML module disabled)")


# -----------------------------
# HOME ROUTE
# -----------------------------
@app.route("/")
def home():
    return jsonify({
        "project": "SSDD - SAST DAST ML Security System",
        "status": "Running Successfully",
        "message": "System Active - Ready for Attack Detection Demo"
    })


# -----------------------------
# SIMULATION TEST (DAST + FGSM)
# -----------------------------
@app.route("/test", methods=["GET"])
def test_attack():

    data = load_digits()
    sample = data.data[0]

    if not validate_input(sample):
        return jsonify({
            "status": "failed",
            "error": "Invalid input detected"
        })

    attacked_sample = add_noise(sample)
    result = detect_attack(attacked_sample)

    return jsonify({
        "mode": "DAST Simulation",
        "attack_type": "FGSM Noise",
        "result": str(result),
        "description": "Attack simulated on sample dataset"
    })


# -----------------------------
# LIVE INPUT DETECTION (FOR VIVA)
# -----------------------------
@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json() or request.form
    input_data = data.get("input")

    if not input_data:
        return jsonify({
            "status": "error",
            "message": "No input provided"
        })

    # Validate input (SAST-like check)
    if not validate_input(input_data):
        return jsonify({
            "status": "blocked",
            "result": "Malicious Input Detected (SAST Validation)"
        })

    # ML / Detection Engine
    result = detect_attack(input_data)

    return jsonify({
        "mode": "Live Detection",
        "input": input_data,
        "result": str(result)
    })


# -----------------------------
# RUN SERVER
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)