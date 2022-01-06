from rest_framework.viewsets import ModelViewSet
from .models import Funcionario
from .serializers import FuncionarioSerializer

class FuncionarioViewSet(ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer