# FinanceFlash

FinanceFlash is a Python server that fetches the latest stock market news and sends email updates. It uses Flask for the server, smtplib for sending emails, and requests for fetching news.

## Features
- Python Flask server to handle requests
- Fetches stock market news via the Finnhub API
- Sends email updates with the latest news
- Predicts the probability of stock price going up by more than 2% using machine learning
- Real-time stock data using free available API

## Setup Instructions
1. **Clone the repository**:
    ```bash
    git clone https://github.com/bestin-07/FinanceFlash.git
    cd FinanceFlash
    ```

2. **Install required dependencies**:
    ```bash
    pip install Flask requests websocket-client scikit-learn pandas
    ```

3. **Configure API keys and email credentials**:
    - Set up your API keys and email credentials in the [config.py] file:
    ```python
    # config.py
    FINHUB_API_KEY = 'your_finnhub_api_key'
    ALPHA_VANTAGE_API_KEY = 'your_alpha_vantage_api_key'

    SMTP_SERVER = 'smtp.gmail.com'
    SMTP_PORT = 587
    EMAIL_ADDRESS = 'your_email@gmail.com'
    EMAIL_PASSWORD = 'your_email_password'
    ```

4. **Run the server**:
    ```bash
    python app.py
    ```

## Usage
- Send a POST request to `/send_email` with the recipient's email address and the category of news (e.g., `general` or `merger`).
- Send a POST request to `/predict_confidence` with the stock symbol to get the probability of the stock price going up by more than 2%.

## Dependencies
- Flask
- requests
- websocket-client
- scikit-learn
- pandas
- smtplib (built-in)

## API
- [Finnhub API](https://finnhub.io/docs/api) for fetching stock market news and real-time data
- [Alpha Vantage API](https://www.alphavantage.co/documentation/) for fetching historical stock market data

## Project Website
- [FinanceFlash](https://financeflash.pythonanywhere.com/)
