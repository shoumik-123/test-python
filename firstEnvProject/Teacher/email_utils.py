from django.core.mail import send_mail
from django.conf import settings


def send_email(subject, message, recipient_list, from_email=settings.DEFAULT_FROM_EMAIL):
    send_mail(
        subject,
        message,
        from_email,
        recipient_list,
        fail_silently=False,
    )




