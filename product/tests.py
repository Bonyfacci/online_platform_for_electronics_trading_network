from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from product.models import Product


class ProductTestCase(APITestCase):
    """
    Для тестирования продукта (Product)
    """

    def setUp(self):
        self.product = Product.objects.create(
            name='TestProduct',
            model='TestModel',
            date_of_release='2023-01-01'
        )

    def test_get_product(self):
        """
        Тест ProductListView
        """
        response = self.client.get(
            reverse('product:products')
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            Product.objects.all().count(),
            1
        )

        self.assertContains(
            response,
            'TestProduct'
        )
