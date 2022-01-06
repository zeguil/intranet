from django.db import models
from uuid import uuid4
from setor.models import Setor

class Corporativo(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    imei = models.CharField(max_length=240)
    marca = models.CharField(max_length=60)
    modelo = models.CharField(max_length=60)
    numero = models.CharField(max_length=60)
    nome = models.CharField(max_length=60)
    setor_id = models.ForeignKey(Setor,on_delete=models.CASCADE)
    state = models.IntegerField(default=0)

    def __str__(self):
        return self.imei