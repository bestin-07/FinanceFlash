import numpy as np
import joblib
from scipy.stats import norm

# Calculate confidence scores
def calculate_confidence(model_path, input_data):
    model = joblib.load(model_path)
    predictions = model.predict(input_data)
    residuals = input_data['Close'] - predictions
    std_dev = np.std(residuals)
    confidence_intervals = norm.interval(0.95, loc=predictions, scale=std_dev)
    return confidence_intervals

if __name__ == "__main__":
    input_data = np.array([[100, 110, 90, 1000000]])  # Example input data
    confidence = calculate_confidence('stock_model.pkl', input_data)
    print("Confidence Interval:", confidence)