from django.db import models

from product.models import Product

NULLABLE = {'null': True, 'blank': True}


class Organization(models.Model):
    """
    Организация
    """
    name = models.CharField(max_length=150, verbose_name='Название организации', help_text='Name of the organization')
    email = models.EmailField(
        verbose_name='Email-адрес',
        help_text='example@mail.com, 150 characters or fewer. Letters, digits and @/./+/-/_ only.'
    )
    postcode = models.PositiveIntegerField(verbose_name='Почтовый индекс', help_text='Postcode, Example:08860')
    country = models.CharField(max_length=50, verbose_name='Страна', help_text='County, Example:Spain')
    city = models.CharField(max_length=50, verbose_name='Город', help_text='City, Example:Barcelona')
    street = models.CharField(max_length=100, verbose_name='Улица', help_text='Street, Example:Passeig Maritim')
    house = models.CharField(max_length=10, verbose_name='Дом', help_text='House, Example:11')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'
        ordering = ['name']


class TradingNetwork(models.Model):
    """
    Торговая сеть
    """
    ORGANIZATION_TYPES = (
        (0, 'Factory'),
        (1, 'Retail network'),
        (2, 'Individual entrepreneur'),
    )

    organization_type = models.IntegerField(
        choices=ORGANIZATION_TYPES,
        verbose_name='Тип организации'
    )

    contacts = models.ForeignKey(
        Organization,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Контакты',
        related_name='contacts_organization'
    )
    products = models.ManyToManyField(
        Product,
        verbose_name='Продукты'
    )
    supplier = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        **NULLABLE,
        verbose_name='Поставщик',
        related_name='product_supplier'
    )

    debit = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.0,
        verbose_name='Задолженность перед поставщиком'
    )

    def __str__(self):
        return self.contacts.name

    class Meta:
        verbose_name = 'Торговая сеть'
        verbose_name_plural = 'Торговые сети'
        ordering = ['pk']
