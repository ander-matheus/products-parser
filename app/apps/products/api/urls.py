from products_parser.contrib.rest_framework.api_router import Router

from .views import ProductViewSet

router = Router()

router.register("products", ProductViewSet, basename="api-products")
urlpatterns = router.urls
