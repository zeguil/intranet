from rest_framework.permissions import BasePermission

class IsPublisher(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj):
        if request.user.publisher:
            return True
        return obj.author == request.user

        