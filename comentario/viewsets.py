from rest_framework.viewsets import ModelViewSet
from .models import Comentario
from .serializers import ComentarioSerializer
from rest_framework.filters import SearchFilter


class ComentarioViewSet(ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
    filter_backends = [SearchFilter]
    search_fields = ['com_nome']