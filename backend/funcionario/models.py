from django.db import models
from setor.models import Setor
from uuid import uuid4


class Funcionario(models.Model):
    func_nome = models.CharField(max_length=60)
    dia_nasc = models.IntegerField()
    mes_nasc = models.CharField(max_length=20)
    setor_id = models.ForeignKey(Setor, on_delete=models.CASCADE)
    state = models.BooleanField()

    def __str__(self):
        return self.nome