from rest_framework.viewsets import ModelViewSet
from .models import Informativo
from .serializers import InformativoSerializer
from rest_framework.filters import SearchFilter

class InformativoViewSet(ModelViewSet):
    queryset = Informativo.objects.all()
    serializer_class = InformativoSerializer
    filter_backends = [SearchFilter]
    search_fields = ['titulo']