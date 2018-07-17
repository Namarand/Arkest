from rest_framework import permissions


class HasApiRight(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser or request.user.groups.filter(name="ApiUser").count():
            return True
        return request.method in permissions.SAFE_METHODS and request.user.groups.filter(name="ApiViewer").count()
