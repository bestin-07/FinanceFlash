# FinanceFlash

FinanceFlash is a Python server that fetches the latest stock market news and sends email updates. It uses Flask for the server, smtplib for sending emails, and requests for fetching news.

## Features
- Python Flask server to handle requests
- Fetches stock market news via an API
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
    - Set up your email credentials in the `config.py` file.
    - Replace the API endpoint with a valid stock news API.

4. **Run the server**:
    ```bash
    python app.py
    ```

## Usage
- Send a POST request to `/send_email` with the recipient's email address.
- The server will fetch the latest stock news and send it via email.

## Dependencies
- Flask
- requests
- smtplib (built-in)

## Contributing
Feel free to contribute and improve the project by submitting pull requests or opening issues.

## License
This project is licensed under the MIT License.
