from rest_framework.serializers import ModelSerializer
from .models import Audit

class AuditSerializer(ModelSerializer):
    class Meta:
        model = Audit
        fields = '__all__'

#tabela
#createdon
#ip
#action
#hostname
#usuario 
#id_tab

