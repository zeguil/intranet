from rest_framework.viewsets import ModelViewSet
from .models import Funcionario
from .serializers import FuncionarioSerializer
from rest_framework.filters import SearchFilter
from rest_framework import permissions

class FuncionarioViewSet(ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
    filter_backends = [SearchFilter]
    search_fields = ['nome']
    permission_classes = (permissions.IsAdminUser, )