from config import EMAIL_ADDRESS, EMAIL_PASSWORD, SMTP_SERVER, SMTP_PORT
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(to_email, email_content):

    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = to_email
    msg['Subject'] = "Stock News Update"

    msg.attach(MIMEText(email_content, 'html'))

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT, timeout=30)  # Increase timeout to 30 seconds
        server.starttls()
        try:
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        except smtplib.SMTPAuthenticationError:
            print("Failed to authenticate with the SMTP server. Check your email address and password.")
            return
        server.sendmail(EMAIL_ADDRESS, to_email, msg.as_string())
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
