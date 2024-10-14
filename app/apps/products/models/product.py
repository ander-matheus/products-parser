from django.db import models


class Product(models.Model):
    TRASH, DRAFT, PUBLISHED = "trash", "draft", "published"
    STATUS_CHOICES = [
        (TRASH, TRASH),
        (DRAFT, DRAFT),
        (PUBLISHED, PUBLISHED),
    ]

    code = models.CharField(max_length=50)
    imported_t = models.DateTimeField(auto_now_add=True)
    url = models.URLField(max_length=255)
    creator = models.TextField()
    created_t = models.BigIntegerField(blank=True, null=True)
    last_modified_t = models.BigIntegerField(blank=True, null=True)
    product_name = models.TextField()
    quantity = models.TextField(blank=True, null=True)
    brands = models.TextField(blank=True, null=True)
    categories = models.TextField(blank=True, null=True)
    labels = models.TextField(blank=True, null=True)
    cities = models.TextField(blank=True, null=True)
    purchase_places = models.TextField(blank=True, null=True)
    ingredients_text = models.TextField(blank=True, null=True)
    traces = models.TextField(blank=True, null=True)
    stores = models.TextField(blank=True, null=True)
    serving_size = models.TextField(blank=True, null=True)
    serving_quantity = models.CharField(max_length=4, blank=True, null=True)
    nutriscore_score = models.CharField(max_length=4, blank=True, null=True)
    nutriscore_grade = models.CharField(max_length=2, blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    image_url = models.URLField(max_length=500)
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default=DRAFT)

    class Meta:
        ordering = ["-pk"]

    def __str__(self) -> str:
        return self.code.__str__()
