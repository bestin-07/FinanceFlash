from stock_analysis.stock_prediction import train_model, predict, load_data
import pandas as pd
import requests
from config import FINHUB_API_KEY


def get_latest_stock_data(symbol):
    url = (
        f'https://finnhub.io/api/v1/quote?symbol={symbol}&token='
        f'{FINHUB_API_KEY}'
    )
    response = requests.get(url)
    data = response.json()
    if 'c' not in data:
        error_message = data.get('error', 'Unknown error')
        raise ValueError(f"Error {symbol}: {error_message}")
    return data


def predict_confidence_percentage(symbol):
    # Load historical data and train the model
    data = load_data(symbol)
    train_model(data)

    # Fetch the latest stock data from Finnhub
    latest_data = get_latest_stock_data(symbol)

    # Prepare input data for prediction
    input_data = pd.DataFrame({
        'open': [latest_data['o']],
        'high': [latest_data['h']],
        'low': [latest_data['l']],
        'close': [latest_data['c']],
    })
    modelpath = 'stock_analysis/stock_model.pkl'

    # Predict the probability of stock price going up more than 5%
    prediction_prob = predict(modelpath, input_data)
    return prediction_prob
