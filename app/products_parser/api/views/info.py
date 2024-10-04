import time

import psutil
from django.db import connection

# from django_celery_beat.models import PeriodicTask
from rest_framework.response import Response
from rest_framework.views import APIView


def check_db_connection():
    try:
        connection.ensure_connection()
        return "up"
    except Exception as e:
        print(e)
        return "down"


class InfoAPIView(APIView):
    def get(self, request, format=None):
        # Get system uptime
        boot_time_timestamp = (
            psutil.boot_time()
        )  # returns boot time in seconds since the epoch
        uptime_seconds = time.time() - boot_time_timestamp
        uptime_str = time.strftime("%H:%M:%S", time.gmtime(uptime_seconds))

        # Get memory usage
        memory_info = psutil.virtual_memory()

        db_connection = check_db_connection()

        last_cron_execution = None

        return Response(
            {
                "db_connection": db_connection,
                "uptime": f"{uptime_seconds} seconds ({uptime_str})",
                "total_memory": f"{memory_info.total / (1024 ** 3):.2f} GB",
                "avaliable_memory": f"{memory_info.available / (1024 ** 3):.2f} GB",
                "used_memory": f"{memory_info.used / (1024 ** 3):.2f} GB",
                "memory_percentage": f"{memory_info.percent}%",
                "last_cron_execution": last_cron_execution,
            }
        )
