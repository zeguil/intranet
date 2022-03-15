from .models import User
from .serializers import UserSerializer
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from pprint import pprint
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import BasePermission

class IsPublisher(BasePermission):

    def has_permission(self, request, view):
        if request.user.publisher == True or request.user.admin == True:
            return True
        

class UsuariosViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes=[IsPublisher]
    queryset = User.objects.all()


    