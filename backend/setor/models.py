from django.db import models
from uuid import uuid4


class Setor(models.Model):

    set_nome = models.CharField(max_length=60)
    state = models.IntegerField(default=0)
    rank = models.IntegerField(null=True)

    def __str__(self):
        return f'<Setor: {self.set_nome}>'