from rest_framework.serializers import ModelSerializer
from .models import Ramal

class RamalSerializer(ModelSerializer):
    class Meta:
        model = Ramal
        fields = "__all__"