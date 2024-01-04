from django.views.generic import ListView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from product.models import Product
from product.serializers import ProductSerializer
from users.permissions import IsActive, IsSuperuser


class ProductViewSet(ModelViewSet):
    """
    Набор представлений (get, create, update) и действий (partial_update, destroy, list) Продукта
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsActive | IsSuperuser]


class ProductListView(ListView):
    """
    Представление списка продуктов
    """
    model = Product
