import aiosmtplib
from email.message import EmailMessage
from config import SMTP_CONFIG

async def send_email(to_email: str, subject: str, body: str):
    """
    Sends an email using SMTP.
    :param to_email: Recipient's email address
    :param subject: Email subject
    :param body: Email body
    :return: Success or error message
    """
    message = EmailMessage()
    message["From"] = SMTP_CONFIG["username"]
    message["To"] = to_email
    message["Subject"] = subject
    message.set_content(body)

    try:
        # Send the email using SMTP
        await aiosmtplib.send(
            message,
            hostname=SMTP_CONFIG["host"],
            port=SMTP_CONFIG["port"],
            username=SMTP_CONFIG["username"],
            password=SMTP_CONFIG["password"],
            use_tls=False,
            start_tls=True,
        )
        return {"status": "success", "message": f"Email sent to {to_email}"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
