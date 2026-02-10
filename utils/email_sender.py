import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os
load_dotenv()

sender_email = os.getenv("SENDER_EMAIL")
password = os.getenv("PASSWORD")

def send_email(receiver_email: str, subject: str, content: str) -> str:
    """
    Send an email using Gmail SMTP.

    Args:
        receiver_email: The email address of the recipient.
        subject: The subject of the email.
        content: The body content of the email.
    """
    # Create the email
    msg = EmailMessage()
    msg["From"] = sender_email
    msg["To"] =  receiver_email
    msg["Subject"] = subject
    msg.set_content(content)

    # Send the email
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, password)
        server.send_message(msg)

print("Email sent!")