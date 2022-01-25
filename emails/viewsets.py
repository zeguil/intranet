from rest_framework.viewsets import ModelViewSet
from .models import Email
from .serializers import EmailSerializer
from rest_framework.filters import SearchFilter

class EmailViewSet(ModelViewSet):
    queryset = Email.objects.all()
    serializer_class = EmailSerializer
    filter_backends = [SearchFilter]
    search_fields = ['email', 'responsavel']