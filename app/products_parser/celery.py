import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "products_parser.settings")

app = Celery("products_parser")

app.config_from_object("products_parser.settings", namespace="CELERY")

app.autodiscover_tasks()


app.conf.beat_schedule = {
    "get_importer_list": {
        "task": "get_importer_list",
        "schedule": crontab(minute="*/5"),  # crontab(minute="0", hour="*/1"),
    },
}


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f"Request: {self.request!r}")
