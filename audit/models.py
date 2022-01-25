from django.contrib.auth.models import User
from django.db import models


class Audit(models.Model):

    tabela = models.CharField(max_length=60)
    createdon = models.DateField(auto_now_add=True)
    ip = models.CharField(max_length=60)
    action = models.CharField(max_length=240)
    hostname = models.CharField(max_length=60)
    usuario = models.CharField(max_length=60)
    id_tab = models.IntegerField()

    def __str__(self):
        return f'<Audit: {self.id}>'