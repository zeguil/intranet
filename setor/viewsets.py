from rest_framework.viewsets import ModelViewSet
from .models import Setor
from .serializers import SetorSerializer
from rest_framework.filters import SearchFilter

class SetorViewSet(ModelViewSet):
    queryset = Setor.objects.all()
    serializer_class = SetorSerializer
    filter_backends = [SearchFilter]
    search_fields = ['set_nome']