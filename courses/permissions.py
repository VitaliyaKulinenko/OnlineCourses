from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user


class Isteacher(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.groups.filter(name='teacher'):
            return True
        return False


class Isstudent(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.groups.filter(name='student'):
            return True
        return False

