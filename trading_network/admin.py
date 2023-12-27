from django.contrib import admin

from trading_network.models import Organization, TradingNetwork


@admin.action(description="Очистка задолженности")
def clear_debit(queryset):
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
    list_filter = ('name',)
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
    list_filter = ('organization_type', 'contacts__name', 'contacts__country', 'contacts__city',)
    search_fields = ('contacts__name', 'contacts__country', 'supplier',)
    actions = [clear_debit]
