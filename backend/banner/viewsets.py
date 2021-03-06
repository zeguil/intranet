from rest_framework.viewsets import ModelViewSet
from .models import Banner
from .serializers import BannerSerializer
from rest_framework.filters import SearchFilter
from rest_framework import permissions
from config.permissions import IsPublisher

class BannerViewSet(ModelViewSet):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer
    filter_backends = [SearchFilter]
    search_fields = ['titulo']
    
    permission_classes_by_action = {
    'create': [IsPublisher],
    'list': [permissions.AllowAny],
    'retrieve': [IsPublisher],
    'update': [IsPublisher],    
    'destroy': [IsPublisher, ]
    }