from rest_framework import serializers

from trading_network.models import TradingNetwork, Organization
from trading_network.validators import debit_change_validator, trading_network_validator


class OrganizationSerializer(serializers.ModelSerializer):
    """
    Сериализатор Организации для представления полей.
    """

    class Meta:
        model = Organization
        fields = '__all__'


class TradingNetworkSerializer(serializers.ModelSerializer):
    """
    Сериализатор Торговой сети для представления полей.
    Валидация данных: иерархия торговой сети и запрет изменения поля «Задолженность перед поставщиком».
    """

    class Meta:
        model = TradingNetwork
        fields = '__all__'
        validators = [trading_network_validator, debit_change_validator]
