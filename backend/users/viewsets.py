from .models import User
from .serializers import UserSerializer
from rest_framework import viewsets, generics
from rest_framework import permissions



class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    permission_classes = (permissions.IsAdminUser, )
