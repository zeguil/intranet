from django.db import models
from setor.models import Setor
from uuid import uuid4


class Ramal(models.Model):

    subsetor = models.CharField(max_length=60)
    responsavel = models.CharField(max_length=120)
    ramal = models.CharField(max_length=20)
    setor_id = models.ForeignKey(Setor, on_delete=models.CASCADE)
    state = models.IntegerField(default=0)
    isBoss = models.BooleanField(default=False, null=True)
    rank = models.IntegerField(null=True)

    def __str__(self):
        return f'<Ramal: {self.ramal}>'