import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Event_booking_system.settings')

app = Celery('Event_booking_system')

# Set the timezone for the Celery app
app.conf.update(timezone='Asia/Kolkata')

# Load Celery configuration from Django settings
app.config_from_object('django.conf:settings', namespace='CELERY')

# Define the Celery beat schedule
app.conf.beat_schedule = {
    "send-mail-every-day-at-8": {
        'task': 'app.task.send_mail_func',
        'schedule': crontab(minute='*/1'),
    }
}

# Load task modules from all registered Django app configs
app.autodiscover_tasks()

# Enable broker connection retry on startup (optional)
app.conf.broker_connection_retry_on_startup = True

