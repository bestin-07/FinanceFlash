from flask import Flask, request, jsonify, render_template
from processor import predict_confidence_percentage
from utils.email_sender import send_email
from utils.stock_news import fetch_news
import smtplib
import requests
from config import FINHUB_API_KEY

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/symbol_suggestions')
def symbol_suggestions():
    query = request.args.get('query')
    if not query:
        return jsonify([])

    url = (
        f'https://finnhub.io/api/v1/search?q={query}&exchange=US&token='
        f'{FINHUB_API_KEY}'
    )
    response = requests.get(url)
    data = response.json()
    suggestions = [result['symbol'] for result in data.get('result', [])]
    return jsonify(suggestions)


@app.route('/predict_confidence', methods=['POST'])
def predict_confidence():
    stock_symbol = request.form.get('stock_symbol')
    print(stock_symbol)
    if not stock_symbol:
        return render_template('error.html'), 400

    prediction = predict_confidence_percentage(stock_symbol)

    return render_template('confidence_result.html', prediction=prediction)


@app.route('/send_email', methods=['POST'])
def send_email_route():
    email = request.form.get('email')
    category = request.form.get('category')
    if not email or not category:
        return render_template('error.html'), 400

    news_items = fetch_news(category)
    email_content = render_template('email_template.html',
                                    stock_news=news_items)
    try:
        send_email(email, email_content)
        return render_template('success.html'), 200
    except (smtplib.SMTPException, TimeoutError, ConnectionRefusedError) as e:
        print(f"Failed to send email: {e}")
        return render_template('error.html'), 500


if __name__ == '__main__':
    app.run(debug=True)
