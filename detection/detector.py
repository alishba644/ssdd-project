import numpy as np

def detect_attack(input_data):
    if np.max(input_data) > 20:
        return "Adversarial Detected"
    return "Normal Input"