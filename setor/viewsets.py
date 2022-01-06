from rest_framework.viewsets import ModelViewSet
from .models import Setor
from .serializers import SetorSerializer

class SetorViewSet(ModelViewSet):
    queryset = Setor.objects.all()
    serializer_class = SetorSerializer