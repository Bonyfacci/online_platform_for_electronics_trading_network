from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    """
    Пользователь
    """
    username = None

    email = models.EmailField(
        unique=True,
        verbose_name='Email-адрес',
        help_text='example@mail.com, 150 characters or fewer. Letters, digits and @/./+/-/_ only.'
    )

    first_name = models.CharField(
        max_length=50,
        verbose_name='Имя',
        help_text='User name. 50 characters or fewer.'
    )
    last_name = models.CharField(
        max_length=50,
        verbose_name='Фамилия',
        **NULLABLE,
        help_text='User last name. 50 characters or fewer.'
    )
    middle_name = models.CharField(
        max_length=50,
        verbose_name='Отчество',
        **NULLABLE,
        help_text='User middle name. 50 characters or fewer.'
    )

    organization = models.CharField(
        max_length=150,
        verbose_name='Организация',
        **NULLABLE,
        help_text='Factory, retail network or individual entrepreneur'
    )

    phone = models.CharField(max_length=18, verbose_name='Номер телефона', **NULLABLE, help_text='Phone number')
    country = models.CharField(max_length=100, verbose_name='Страна', **NULLABLE, help_text='Country')
    city = models.CharField(max_length=100, verbose_name='Город', **NULLABLE, help_text='City')
    avatar = models.ImageField(upload_to='users/', verbose_name='Аватар', **NULLABLE, help_text='Avatar or foto')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('pk',)

