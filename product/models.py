from django.db import models


NULLABLE = {'null': True, 'blank': True}


class Product(models.Model):
    """
    Модель Продукт (Название, Модель, Дата выхода продукта на рынок)
    """
    name = models.CharField(
        max_length=150,
        verbose_name='Наименование товара',
        help_text='Name of product'
    )
    model = models.CharField(
        max_length=150,
        verbose_name='Модель продукта',
        help_text='Model of product'
    )
    date_of_release = models.DateField(
        verbose_name='Дата выхода продукта на рынок',
        help_text='Date of release'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания продукта',
        help_text='Date of release'
    )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
