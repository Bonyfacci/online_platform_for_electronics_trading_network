from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from trading_network.models import Organization, TradingNetwork
from trading_network.validators import trading_network_validator


@admin.action(description="Очистка задолженности")
def clear_debit(_, model, queryset):
    """
    Очищающая задолженность перед поставщиком у выбранных объектов
    """
    queryset.update(debit=0)


@admin.register(Organization)
class OrganizationsListAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'email',
        'postcode',
        'country',
        'city',
        'street',
        'house'
    )
    list_filter = ('country', 'city',)
    search_fields = ('name', 'email', 'country', 'city',)


@admin.register(TradingNetwork)
class TradingNetworkListAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'organization_type',
        'contacts',
        'supplier',
        'debit',
    )
    list_filter = ('organization_type', 'contacts__country', 'contacts__city',)
    search_fields = ('contacts__name', 'contacts__country', 'supplier',)

    actions = [clear_debit]

    list_display_links = ('supplier',)

    def supplier(self, obj):
        supplier = obj.supplier
        if supplier:
            url = reverse('admin:suppliers_network', args=[supplier.pk])
            return format_html('<a href="{}">{}</a>', url, supplier.name)
        return 'Завод не поставляет'

    supplier.short_description = 'Поставщик'

    def save_form(self, request, form, change):
        validators = [trading_network_validator]
        for item in validators:
            item(form.cleaned_data)
        return form.save(commit=False)
