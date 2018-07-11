from rest_framework import permissions


class IsApiUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.groups.filter(name="ApiUser").count()

class IsApiViewer(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.method == 'GET' or request.user.groups.filter(name="ApiViewer").count()
