from .models import User
from .serializers import UserSerializer
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAdminUser

from rest_framework.decorators import permission_classes

        

class UsuariosViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes=[IsAdminUser]
    queryset = User.objects.all()


    