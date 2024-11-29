# apps/taxi/permissions.py
from rest_framework import permissions


class IsActiveUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_active
