from rest_framework.viewsets import ModelViewSet
from .models import Banner
from .serializers import BannerSerializer
from rest_framework.filters import SearchFilter


class BannerViewSet(ModelViewSet):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer
    filter_backends = [SearchFilter]
    search_fields = ['titulo']