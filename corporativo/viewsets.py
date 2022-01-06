from rest_framework.viewsets import ModelViewSet
from .models import Corporativo
from .serializers import CorporativoSerializer

class CorporativoViewSet(ModelViewSet):
    queryset = Corporativo.objects.all()
    serializer_class = CorporativoSerializer