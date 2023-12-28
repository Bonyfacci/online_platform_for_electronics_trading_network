from rest_framework import serializers

from trading_network.models import TradingNetwork, Organization


class OrganizationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organization
        fields = '__all__'


class TradingNetworkSerializer(serializers.ModelSerializer):

    class Meta:
        model = TradingNetwork
        fields = '__all__'
