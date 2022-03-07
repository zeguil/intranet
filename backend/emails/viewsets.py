from rest_framework.viewsets import ModelViewSet
from .models import Email
from .serializers import EmailSerializer
from rest_framework.filters import SearchFilter
from rest_framework import permissions

class EmailViewSet(ModelViewSet):
    queryset = Email.objects.all()
    serializer_class = EmailSerializer
    filter_backends = [SearchFilter]
    search_fields = ['email', 'responsavel']
    permission_classes_by_action = {'create': [permissions.IsAdminUser],   
                                    'list': [permissions.AllowAny]}