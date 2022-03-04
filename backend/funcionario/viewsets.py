from rest_framework.viewsets import ModelViewSet
from .models import Funcionario
from .serializers import FuncionarioSerializer
from rest_framework.filters import SearchFilter

class FuncionarioViewSet(ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
    filter_backends = [SearchFilter]
    search_fields = ['nome']