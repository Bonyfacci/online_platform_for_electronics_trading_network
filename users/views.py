from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated

from users.models import User
from users.permissions import IsOwner, IsSuperuser
from users.serializers import UserSerializer, UserCreateSerializer


class UserCreateAPIView(generics.CreateAPIView):
    """
    Представление для создания пользователя
    """
    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()


class UserListAPIView(generics.ListAPIView):
    """
    Представление для получения списка пользователей
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """
    Представление для получения экземпляра пользователя
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


class UserUpdateAPIView(generics.UpdateAPIView):
    """
    Представление для обновления пользователя
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsOwner]


class UserDestroyAPIView(generics.DestroyAPIView):
    """
    Представление для удаления пользователя
    """
    queryset = User.objects.all()
    permission_classes = [IsSuperuser]
