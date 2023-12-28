from django.contrib import admin

from product.models import Product


@admin.register(Product)
class ProductsListAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'model', 'date_of_release',)
    list_filter = ('name',)
    search_fields = ('name', 'model',)
