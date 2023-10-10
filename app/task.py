from django.contrib.auth import get_user_model
from celery import  shared_task
from django.core.mail import send_mail
from Event_booking_system import settings
    # users=get_user_model().objects.all()
    # for user in users:
import logging
logger = logging.getLogger(__name__)
@shared_task(bind=True)
def send_mail_func(self):
    try:
        mail_sub = "Hey celery testing"
        message = "Like this email config in django"
        to_mail = "vikashgusain1999@gmail.com"
        send_mail(
            subject=mail_sub,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[],
            fail_silently=True
        )
        return {
            "TET": "UUID",
            "SUER": "IMp_DATA"
        }
    except Exception as e:
        logger.error(f"An error occurred while sending the email: {str(e)}")
        return str(e)