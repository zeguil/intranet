from rest_framework.serializers import ModelSerializer
from .models import Corporativo

class CorporativoSerializer(ModelSerializer):
    class Meta:
        model = Corporativo
        fields = '__all__'