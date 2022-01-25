from django.db import models
from administrador.models import Administrador
from datetime import datetime
from uuid import uuid4


class Informativo(models.Model):

    titulo = models.CharField(max_length=60)
    link = models.CharField(max_length=240)
    image = models.ImageField(upload_to='informativos', blank=True, null=True )
    data_pub = models.DateField(default=datetime.today())
    state = models.IntegerField(default=0)
    admin_id = models.ForeignKey(Administrador, on_delete=models.CASCADE)

    def __str__(self):
        return f'<Informativo: {self.titulo}>'