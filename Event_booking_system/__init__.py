from __future__ import absolute_import, unicode_literals

# Import the Celery application instance
from .celery import app as celery_app

# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
__all__ = ('celery_app',)


# celery -A Event_booking_system worker --loglevel=info
# celery -A Event_booking_system beat -l INFO
