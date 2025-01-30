from flask import Flask, request, jsonify
from utils.stock_news import fetch_stock_news
from utils.email_sender import send_email

app = Flask(__name__)

@app.route('/send_email', methods=['POST'])
def send_email_route():
    data = request.json
    email = data['email']
    stock_news = fetch_stock_news()
    send_email(email, stock_news)
    return jsonify({'message': 'Email sent successfully!'})

if __name__ == '__main__':
    app.run(debug=True)