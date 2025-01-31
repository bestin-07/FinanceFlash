# FinanceFlash

FinanceFlash is a Python server that fetches the latest stock market news and sends email updates. It uses Flask for the server, smtplib for sending emails, and requests for fetching news.
Since I use open souce servers, the functionality could be no efficient.

## Features
- Python Flask server to handle requests
- Fetches stock market news via the Finnhub API
- Sends email updates with the latest news

## Setup Instructions
1. **Clone the repository**:
    ```bash
    git clone https://github.com/bestin-07/FinanceFlash.git
    cd FinanceFlash
    ```

2. **Install required dependencies**:
    ```bash
    pip install Flask requests
    ```

3. **Configure email credentials and API endpoint**:
    - Set up your email credentials in the [config.py](http://_vscodecontentref_/2) file.
    - Replace the API endpoint with a valid stock news API from Finnhub.

4. **Run the server**:
    ```bash
    python app.py
    ```

## Usage
- Send a POST request to `/send_email` with the recipient's email address and the category of news (e.g., `general` or `merger`).
- The server will fetch the latest stock news from Finnhub and send it via email.

## Dependencies
- Flask
- requests
- smtplib (built-in)

## API
- [Finnhub API](https://finnhub.io/docs/api) for fetching stock market news

## Project Website
- [FinanceFlash](https://financeflash.pythonanywhere.com/)
