from rest_framework.pagination import PageNumberPagination


class OrganizationPaginator(PageNumberPagination):
    """
    Стиль представления организаций по страницам
    """
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 15


class TradingNetworkPaginator(PageNumberPagination):
    """
    Стиль представления торговых сетей по страницам
    """
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 15
