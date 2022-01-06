from rest_framework.viewsets import ModelViewSet
from .models import Audit
from .serializers import AuditSerializer

class AuditViewSet(ModelViewSet):
    queryset = Audit.objects.all()
    serializer_class = AuditSerializer