# Generated by Django 5.0 on 2024-01-04 12:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trading_network', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tradingnetwork',
            name='supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_supplier', to='trading_network.tradingnetwork', verbose_name='Поставщик'),
        ),
    ]
