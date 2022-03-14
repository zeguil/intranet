from .models import User
from .serializers import UserSerializer
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from pprint import pprint
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes


class UsuariosViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


    
