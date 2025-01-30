from flask import Flask, request, jsonify, render_template
from utils.stock_news import fetch_news
from utils.email_sender import send_email
import smtplib

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send_email', methods=['POST'])
def send_email_route():
    email = request.form.get('email')
    category = request.form.get('category')
    if not email or not category:
        return render_template('error.html'), 400

    news_items = fetch_news(category)
    email_content = render_template('email_template.html', stock_news=news_items)
    try:
        send_email(email, email_content)
        return render_template('success.html')
    except (smtplib.SMTPException, TimeoutError, ConnectionRefusedError) as e:
        print(f"Failed to send email: {e}")
        return render_template('error.html'), 500

if __name__ == '__main__':
    app.run(debug=True)