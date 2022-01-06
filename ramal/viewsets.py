from rest_framework.viewsets import ModelViewSet
from .models import Ramal
from .serializers import RamalSerializer

class RamalViewSet(ModelViewSet):
    queryset = Ramal.objects.all()
    serializer_class = RamalSerializer