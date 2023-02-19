from rest_framework import permissions


class ActiveUsers(permissions.BasePermission):
    """
    Реализация доступа только для активных пользователей
    """
    def has_permission(self, request, view):
        if request.user.is_active:
            return True
        return False