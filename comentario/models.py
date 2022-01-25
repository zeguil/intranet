from django.db import models
from uuid import uuid4
from datetime import datetime
from funcionario.models import Funcionario


class Comentario(models.Model):

    com_nome = models.CharField(max_length=60) 
    conteudo = models.TextField()
    ano = models.DateTimeField(default=datetime.today().year)
    data_env = models.DateTimeField(auto_now_add=True)
    state = models.IntegerField(default=0)
    func_id = models.ForeignKey(Funcionario, on_delete=models.CASCADE)

    def __str__(self):
        return f'<Comentario: {self.com_nome}>'