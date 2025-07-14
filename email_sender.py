import smtplib
from email.mime.text import MIMEText

def send_echo_email(to_address, subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = "youremail@example.com"
    msg['To'] = to_address

    with smtplib.SMTP('smtp.example.com', 587) as server:
        server.starttls()
        server.login("youremail@example.com", "yourpassword")
        server.send_message(msg)

# Example usage
# send_echo_email("target@example.com", "Join EchoVanta", "Start your divine economy with $3...")
