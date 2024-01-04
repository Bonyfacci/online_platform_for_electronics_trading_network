from rest_framework import serializers

from product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    """
    Сериализатор Продукта для представления полей при реализации create и update.
    """

    class Meta:
        model = Product
        fields = '__all__'
