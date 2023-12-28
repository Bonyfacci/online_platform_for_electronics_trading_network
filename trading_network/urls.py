from django.urls import path

from trading_network.apps import TradingNetworkConfig
from trading_network.views import TradingNetworkCreateAPIView, TradingNetworkListAPIView, TradingNetworkDetailAPIView, \
    TradingNetworkUpdateAPIView, TradingNetworkDeleteAPIView, OrganizationCreateAPIView, OrganizationListAPIView, \
    OrganizationDetailAPIView, OrganizationUpdateAPIView, OrganizationDeleteAPIView

app_name = TradingNetworkConfig.name

urlpatterns = [
    #  TradingNetwork - http://127.0.0.1:8000/trading_network/
    path('create/', TradingNetworkCreateAPIView.as_view(), name='trading_network_create'),
    path('', TradingNetworkListAPIView.as_view(), name='trading_network_list'),
    path('<int:pk>/', TradingNetworkDetailAPIView.as_view(), name='trading_network_detail'),
    path('update/<int:pk>/', TradingNetworkUpdateAPIView.as_view(), name='trading_network_update'),
    path('delete/<int:pk>/', TradingNetworkDeleteAPIView.as_view(), name='trading_network_delete'),

    #  Organization - http://127.0.0.1:8000/trading_network/organizations/
    path('organization/create/', OrganizationCreateAPIView.as_view(), name='organization_create'),
    path('organizations/', OrganizationListAPIView.as_view(), name='organization_list'),
    path('organization/<int:pk>/', OrganizationDetailAPIView.as_view(), name='organization_detail'),
    path('organization/update/<int:pk>/', OrganizationUpdateAPIView.as_view(), name='organization_update'),
    path('organization/delete/<int:pk>/', OrganizationDeleteAPIView.as_view(), name='organization_delete'),
]
