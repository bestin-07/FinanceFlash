from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import requests
from config import ALPHA_VANTAGE_API_KEY


# Load the dataset
def load_data(symbol):
    url = (
        f'https://www.alphavantage.co/query?'
        f'function=TIME_SERIES_DAILY&symbol={symbol}'
        f'&outputsize=full&apikey={ALPHA_VANTAGE_API_KEY}'
    )
    response = requests.get(url)
    data = response.json()

    if 'Time Series (Daily)' not in data:
        error_message = data.get('Error Message', 'Unknown error')
        raise ValueError(f"Error {symbol}: {error_message}")

    # Convert the data to a pandas DataFrame
    df = pd.DataFrame.from_dict(data['Time Series (Daily)'], orient='index')
    df = df.rename(columns={
        '1. open': 'open',
        '2. high': 'high',
        '3. low': 'low',
        '4. close': 'close',
    })
    df.index = pd.to_datetime(df.index)
    df = df.sort_index()

    # Convert columns to numeric types
    df[['open', 'high', 'low', 'close']] = df[['open', 'high', 'low', 'close']].apply(pd.to_numeric)

    # Filter data for the last 15 years
    df = df[df.index >= pd.Timestamp.now() - pd.DateOffset(years=15)]

    return df


# Train the model
def train_model(data):
    # Include relevant features for options chain, IV, and Greeks
    features = ['open', 'high', 'low', 'close']

    X = data[features]
    # 1 if next day's close is more than 5% higher, else 0
    y = ((data['close'].shift(-1) / data['close']) > 1.02).astype(float)
    X = X[:-1]  # Remove the last row to match the shifted target
    y = y[:-1]  # Remove the last row to avoid NaN values

    # Debug: Check the distribution of the target variable
    print("Distribution of target variable 'y':")
    print(y.value_counts())

    # Ensure the target variable has both classes
    if y.nunique() < 2:
        raise ValueError(" 'y' does not have both classes' (0 and 1).")

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,
                                                        random_state=42)

    # Using a more robust model like RandomForestClassifier
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    joblib.dump(model, 'stock_analysis/stock_model.pkl')
    print("Model trained and saved as stock_model.pkl")


# Predict stock price movement
def predict(model_path, input_data):
    model = joblib.load(model_path)
    # Probability of stock price going up more than 2%
    prediction_prob = model.predict_proba(input_data)[:, 1]
    return prediction_prob
