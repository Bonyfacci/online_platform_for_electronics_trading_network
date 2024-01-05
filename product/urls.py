from django.urls import path
from rest_framework.routers import DefaultRouter

from product.apps import ProductConfig
from product.views import ProductViewSet, ProductListView

app_name = ProductConfig.name

router = DefaultRouter()
router.register(r'', ProductViewSet, basename='product')

urlpatterns = [
    path('', ProductListView.as_view(), name='products'),
] + router.urls
