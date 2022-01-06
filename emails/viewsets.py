from rest_framework.viewsets import ModelViewSet
from .models import Email
from .serializers import EmailSerializer

class EmailViewSet(ModelViewSet):
    queryset = Email.objects.all()
    serializer_class = EmailSerializer