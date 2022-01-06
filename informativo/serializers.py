from rest_framework.serializers import ModelSerializer
from .models import Informativo

class InformativoSerializer(ModelSerializer):
    class Meta:
        model = Informativo
        fields = "__all__"