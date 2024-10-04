from rest_framework.viewsets import ModelViewSet

from apps.products.api.serializers import ProductSerializer
from apps.products.models import Product


class ProductViewSet(ModelViewSet):
    http_method_names = ["get", "post", "delete", "put"]

    queryset = Product.objects.exclude(status=Product.TRASH)
    serializer_class = ProductSerializer

    lookup_field = "code"

    def perform_destroy(self, instance):
        instance.status = Product.TRASH
        instance.save()
