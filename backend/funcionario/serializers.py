from rest_framework.serializers import ModelSerializer
from .models import Funcionario
from comentario.serializers import ComentarioSerializer

class FuncionarioSerializer(ModelSerializer):

    comentarios = ComentarioSerializer(many=True, read_only=True)

    class Meta:
        model = Funcionario
        fields = ('func_nome', 'dia_nasc', 'mes_nasc', 'setor_id', 'comentarios')