from .models import User
from .serializers import UserSerializer
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from pprint import pprint
from rest_framework.authentication import TokenAuthentication

class UsuariosViewSet(viewsets.ModelViewSet):
    permissions_classes = (IsAdminUser,)
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsAdminUser, )
    # authentication_classes= (TokenAuthentication, )

    
