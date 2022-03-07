from rest_framework.viewsets import ModelViewSet
from .models import Comentario
from .serializers import ComentarioSerializer
from rest_framework.filters import SearchFilter
from rest_framework import permissions


class ComentarioViewSet(ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
    filter_backends = [SearchFilter]
    search_fields = ['com_nome']
    permission_classes_by_action = {'create': [permissions.IsAdminUser],   
                                    'list': [permissions.AllowAny]}