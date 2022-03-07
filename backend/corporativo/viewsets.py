from rest_framework.viewsets import ModelViewSet
from .models import Corporativo
from .serializers import CorporativoSerializer
from rest_framework.filters import SearchFilter
from rest_framework import permissions


class CorporativoViewSet(ModelViewSet):
    queryset = Corporativo.objects.all()
    serializer_class = CorporativoSerializer
    filter_backends = [SearchFilter]
    search_fields = ['numero']
    permission_classes_by_action = {'create': [permissions.IsAdminUser],   
                                    'list': [permissions.AllowAny]}