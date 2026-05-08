import numpy as np

def detect_attack(input_data):

    try:
        # If input is string → treat as suspicious (SQLi / injection)
        if isinstance(input_data, str):
            return "Suspicious Input Detected (Non-Numeric Attack)"

        # Convert safely to numpy array
        data = np.array(input_data, dtype=float)

        # Simple ML-like rule
        if np.max(data) > 20:
            return "Adversarial Attack Detected"

        return "Normal Input"

    except Exception:
        return "Invalid / Malicious Input Format"