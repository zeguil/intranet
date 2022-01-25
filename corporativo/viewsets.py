from rest_framework.viewsets import ModelViewSet
from .models import Corporativo
from .serializers import CorporativoSerializer
from rest_framework.filters import SearchFilter


class CorporativoViewSet(ModelViewSet):
    queryset = Corporativo.objects.all()
    serializer_class = CorporativoSerializer
    filter_backends = [SearchFilter]
    search_fields = ['numero']