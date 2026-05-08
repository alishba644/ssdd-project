import numpy as np

def add_noise(input_data):
    noise = np.random.normal(0, 0.5, input_data.shape)
    return input_data + noise