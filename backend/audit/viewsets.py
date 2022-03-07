from rest_framework.viewsets import ModelViewSet
from .models import Audit
from .serializers import AuditSerializer
from rest_framework.filters import SearchFilter
from rest_framework import permissions



class AuditViewSet(ModelViewSet):
    queryset = Audit.objects.all()
    serializer_class = AuditSerializer
    filter_backends = [SearchFilter]
    search_fields = ['ip']
    permission_classes_by_action = {'create': [permissions.IsAdminUser],   
                                    'list': [permissions.AllowAny]}