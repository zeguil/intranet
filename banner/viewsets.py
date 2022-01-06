from rest_framework.viewsets import ModelViewSet
from .models import Banner
from .serializers import BannerSerializer

class BannerViewSet(ModelViewSet):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer