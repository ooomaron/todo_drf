from rest_framework import permissions

class TaskAccessPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.id is not None:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.id is not None:
            if obj.author.id == request.user.id:
                return True
            return False
        return False
    