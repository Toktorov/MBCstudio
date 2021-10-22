from django.conf import settings
from django.core.mail import EmailMessage

from MBCstudio.celery import app



@app.task
def send_info(email):
    message = f"""
    Элек.почта: {email}
    """
    email = EmailMessage(
        "Hello",
        message, settings.EMAIL_HOST_USER,
        [email],
    )
    email.send(fail_silently=False)
