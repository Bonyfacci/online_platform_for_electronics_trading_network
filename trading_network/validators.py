from rest_framework.exceptions import ValidationError


def trading_network_validator(value):
    """
    Проверки создания торговой сети по иерархии
    """

    supplier = value.get('supplier')

    if value.get('organization_type') != 0:
        if supplier.organization_type > value.get('organization_type'):
            raise ValidationError('Должна быть соблюдена иерархия торговой сети. '
                                  'Завод -> Розничная сеть -> Индивидуальный предприниматель')


def debit_change_validator(value):
    """
    Проверки изменения поля «Задолженность перед поставщиком»
    """
    if value.get('debit') is not None or float(value.get('debt')) != 0.0:
        raise ValidationError('Запрещено обновление через API поля «Задолженность перед поставщиком»')
