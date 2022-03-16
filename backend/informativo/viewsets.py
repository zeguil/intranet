from rest_framework.viewsets import ModelViewSet
from .models import Informativo
from .serializers import InformativoSerializer
from rest_framework.filters import SearchFilter
from rest_framework import permissions
from config.permissions import IsPublisher

class InformativoViewSet(ModelViewSet):
    queryset = Informativo.objects.all()
    serializer_class = InformativoSerializer
    filter_backends = [SearchFilter]
    search_fields = ['titulo']
    permission_classes_by_action = {
    'create': [IsPublisher],
    'list': [permissions.AllowAny],
    'retrieve': [IsPublisher],
    'update': [IsPublisher],    
    'destroy': [IsPublisher, ]
    }