import joblib
from sklearn.datasets import load_digits
from model.attacks.fgsm import add_noise
from model.detection.detector import detect_attack
from model.detection.sast_scan import sast_scan
from model.detection.dast_scan import dast_scan
from model.validation import validate_input
import os

def main():

    print("SYSTEM STARTED")

    print("SAST:", sast_scan("model/detection/detector.py"))
    print("DAST sample:", dast_scan()[:5])

    if not os.path.exists("model.pkl"):
        print("Model missing")
        return

    model = joblib.load("model.pkl")
    data = load_digits()

    for i in range(10):
        sample = data.data[i]

        if validate_input(sample):
            attacked = add_noise(sample)
            print(detect_attack(attacked))

if _name_ == "_main_":
    main()
    