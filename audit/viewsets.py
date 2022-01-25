from rest_framework.viewsets import ModelViewSet
from .models import Audit
from .serializers import AuditSerializer
from rest_framework.filters import SearchFilter



class AuditViewSet(ModelViewSet):
    queryset = Audit.objects.all()
    serializer_class = AuditSerializer
    filter_backends = [SearchFilter]
    search_fields = ['ip']