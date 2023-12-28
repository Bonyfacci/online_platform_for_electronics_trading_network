from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    message = 'Вы не являетесь владельцем!'

    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner:
            return True
        return False


class IsActive(BasePermission):
    message = 'У Вас нет доступа, обратитесь к администратору!'

    def has_permission(self, request, view):
        if request.user.is_active:
            return True
        return False


class IsSuperuser(BasePermission):
    message = 'Вы не являетесь администратором!'

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        return False
