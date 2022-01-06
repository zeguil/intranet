from django.db import models
from uuid import uuid4
from datetime import datetime
from funcionario.models import Funcionario


class Comentario(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    com_nome = models.CharField(max_length=50) 
    conteudo = models.TextField()
    ano = models.DateField(default=datetime.today().year)
    data_env = models.DateField(auto_now_add=True)
    state = models.IntegerField(default=0)
    func_id = models.ForeignKey(Funcionario, on_delete=models.CASCADE)

    def __str__(self):
        return self.com_nome