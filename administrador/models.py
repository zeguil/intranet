from django.db import models
from uuid import uuid4


class Administrador(models.Model):
    
    usuario = models.CharField(max_length=60, unique=True)
    adm_nome = models.CharField(max_length=60)
    senha_hash = models.CharField(max_length=128)
    is_admin = models.BooleanField(default=False)
    is_publisher = models.BooleanField(default=False) 
