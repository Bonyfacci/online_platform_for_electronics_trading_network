from rest_framework import serializers

from users.models import User


class UserCreateSerializer(serializers.ModelSerializer):
    """
    Сериализатор Пользователя для представления полей при реализации create
    """

    class Meta:
        model = User
        # fields = '__all__'
        fields = (
            'id',
            'email',
            'first_name',
            'organization',
            'country',
        )


class UserSerializer(serializers.ModelSerializer):
    """
    Сериализатор Пользователя для представления полей
    """

    class Meta:
        model = User
        fields = '__all__'
