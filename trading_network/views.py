from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated

from trading_network.models import TradingNetwork, Organization
from trading_network.paginators import TradingNetworkPaginator, OrganizationPaginator
from trading_network.serializers import TradingNetworkSerializer, OrganizationSerializer
from users.permissions import IsActive, IsSuperuser


# ================================================================ TradingNetwork

class TradingNetworkListAPIView(generics.ListAPIView):
    """
    Представление для получения списка торговых сетей
    """
    queryset = TradingNetwork.objects.all()
    serializer_class = TradingNetworkSerializer
    pagination_class = TradingNetworkPaginator
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ('contacts__city',)
    search_fields = ('contacts__city', 'contacts__name',)
    ordering_fields = ('contacts__name',)
    permission_classes = [IsAuthenticated, IsActive | IsSuperuser]


class TradingNetworkCreateAPIView(generics.CreateAPIView):
    """
    Представление для создания торговой сети
    """
    queryset = TradingNetwork.objects.all()
    serializer_class = TradingNetworkSerializer
    permission_classes = [IsAuthenticated, IsActive | IsSuperuser]


class TradingNetworkDetailAPIView(generics.RetrieveAPIView):
    """
    Представление для получения экземпляра торговой сети
    """
    queryset = TradingNetwork.objects.all()
    serializer_class = TradingNetworkSerializer
    permission_classes = [IsAuthenticated, IsActive | IsSuperuser]


class TradingNetworkUpdateAPIView(generics.UpdateAPIView):
    """
    Представление для обновления торговой сети
    """
    queryset = TradingNetwork.objects.all()
    serializer_class = TradingNetworkSerializer
    permission_classes = [IsAuthenticated, IsActive | IsSuperuser]


class TradingNetworkDeleteAPIView(generics.DestroyAPIView):
    """
    Представление для удаления торговой сети
    """
    queryset = TradingNetwork.objects.all()
    serializer_class = TradingNetworkSerializer
    permission_classes = [IsAuthenticated, IsActive | IsSuperuser]


# ================================================================ Organization

class OrganizationListAPIView(generics.ListAPIView):
    """
    Представление для получения списка организаций
    """
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    pagination_class = OrganizationPaginator
    permission_classes = [IsAuthenticated, IsActive | IsSuperuser]


class OrganizationCreateAPIView(generics.CreateAPIView):
    """
    Представление для создания организации
    """
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [IsAuthenticated, IsActive | IsSuperuser]


class OrganizationDetailAPIView(generics.RetrieveAPIView):
    """
    Представление для получения экземпляра организации
    """
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [IsAuthenticated, IsActive | IsSuperuser]


class OrganizationUpdateAPIView(generics.UpdateAPIView):
    """
    Представление для обновления организации
    """
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [IsAuthenticated, IsActive | IsSuperuser]


class OrganizationDeleteAPIView(generics.DestroyAPIView):
    """
    Представление для удаления организации
    """
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [IsAuthenticated, IsActive | IsSuperuser]



