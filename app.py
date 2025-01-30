from flask import Flask, request, jsonify, render_template
from utils.stock_news import fetch_stock_news
from utils.email_sender import send_email
import smtplib

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send_email', methods=['POST'])
def send_email_route():
    email = request.form.get('email')
    if not email:
        return render_template('error.html'), 400

    stock_news = fetch_stock_news()
    email_content = render_template('email_template.html', stock_news=stock_news)
    print(email_content)
    try:
        send_email(email, email_content)
    except (smtplib.SMTPException, TimeoutError, ConnectionRefusedError) as e:
        print(f"Failed to send email: {e}")
        return render_template('error.html'), 500
    else:
        return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)