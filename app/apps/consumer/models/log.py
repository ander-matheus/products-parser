from django.db import models


class ConsumerLog(models.Model):
    IN_PROGRESS, COMPLETED, ERROR = "in progress", "completed", "error"
    STATUS_CHOICE = [
        (IN_PROGRESS, IN_PROGRESS),
        (COMPLETED, COMPLETED),
        (ERROR, ERROR),
    ]

    url = models.URLField(max_length=255)
    created_t = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATUS_CHOICE, default=IN_PROGRESS)
    exception_description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ["-pk"]

    def __str__(self) -> str:
        return f"{self.url} - {self.created_t}"
