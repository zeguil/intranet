from django.db import models
from setor.models import Setor
from comentario.models import Comentario
from uuid import uuid4


class Funcionario(models.Model):
    nome = models.CharField(max_length=60, index=True)
    dia_nasc = models.IntegerField()
    mes_nasc = models.CharField(max_length=20)
    setor_id = models.ForeignKey(Setor, on_delete=models.CASCADE)
    state = models.IntegerField(default=0)
    comentario = models.ForeignKey(Comentario, on_delete=models.CASCADE)

    def __str__(self):
        return self.func_nome