from django.db import models
from administrador.models import Administrador
from uuid import uuid4


class Informativo(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    titulo = models.CharField(max_length=60)
    link = models.CharField(max_length=240)
    foto = models.ImageField(upload_to='informativos', blank=True, null=True )
    data_pub = models.DateField(auto_now_add=True)
    state = models.IntegerField(default=0)
    admin_id = models.ForeignKey(Administrador, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo