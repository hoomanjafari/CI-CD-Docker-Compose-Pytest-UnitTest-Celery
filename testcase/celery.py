import os

from celery import Celery
from celery.schedules import crontab

from index.tasks import test_celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'testcase.settings')

app = Celery('testcase')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.on_after_configure.connect
def test_celery_beat(sender, **kwargs):
    sender.add_periodic_task(
        # crontab(hour=1, minute=30, day_of_week='mon-fri')  this is for specific time
        5, test_celery.s(44), name='test-celery-beat',
    )
