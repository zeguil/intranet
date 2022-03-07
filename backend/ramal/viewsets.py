from rest_framework.viewsets import ModelViewSet
from .models import Ramal
from .serializers import RamalSerializer
from rest_framework.filters import SearchFilter
from rest_framework import permissions

class RamalViewSet(ModelViewSet):
    queryset = Ramal.objects.all()
    serializer_class = RamalSerializer
    filter_backends = [SearchFilter]
    search_fields = ['ramal']
    permission_classes_by_action = {'create': [permissions.IsAdminUser],   
                                    'list': [permissions.AllowAny]}