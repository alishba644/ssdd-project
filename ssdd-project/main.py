import joblib
from sklearn.datasets import load_digits
from attacks.fgsm import add_noise
from detection.detector import detect_attack
from security.validation import validate_input
import os

# Load model safely
if not os.path.exists("model.pkl"):
    print("Error: model.pkl not found. Train the model first.")
    exit()

model = joblib.load("model.pkl")

# Load sample data
data = load_digits()
sample = data.data[0]  # ✅ Fixed

# Validate
if not validate_input(sample):
    print("Invalid input")
    exit()

# Attack
attacked = add_noise(sample)

# Detection
result = detect_attack(attacked)

print("Detection Result:", result)