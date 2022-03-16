from rest_framework.permissions import BasePermission

class IsPublisher(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.user.publisher == True or request.user.admin == True:
                return True
        
class IsComun(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.user.publisher == False and request.user.admin == False:
                return True