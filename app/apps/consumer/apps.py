from django.apps import AppConfig
from django.db.models.signals import post_save


class ConsumerConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.consumer"

    def ready(self) -> None:
        from .models import ConsumerLog
        from .signals import post_save_consumerlog

        post_save.connect(
            post_save_consumerlog,
            sender=ConsumerLog,
            dispatch_uid="post_save_consumerlog",
        )
