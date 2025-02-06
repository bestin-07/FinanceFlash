import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

# Load the dataset
def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

# Train the model
def train_model(data):
    X = data[['Open', 'High', 'Low', 'Volume']]
    y = data['Close']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    joblib.dump(model, 'stock_model.pkl')
    print("Model trained and saved as stock_model.pkl")

# Predict stock prices
def predict(model_path, input_data):
    model = joblib.load(model_path)
    prediction = model.predict(input_data)
    return prediction

if __name__ == "__main__":
    data = load_data('historical_stock_prices.csv')
    train_model(data)