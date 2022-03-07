from rest_framework.viewsets import ModelViewSet
from .models import Setor
from .serializers import SetorSerializer
from rest_framework.filters import SearchFilter
from rest_framework import permissions

class SetorViewSet(ModelViewSet):
    queryset = Setor.objects.all()
    serializer_class = SetorSerializer
    filter_backends = [SearchFilter]
    search_fields = ['set_nome']
    permission_classes_by_action = {'create': [permissions.IsAdminUser],   
                                    'list': [permissions.AllowAny]}