from rest_framework.viewsets import ModelViewSet
from .models import Informativo
from .serializers import InformativoSerializer

class InformativoViewSet(ModelViewSet):
    queryset = Informativo.objects.all()
    serializer_class = InformativoSerializer