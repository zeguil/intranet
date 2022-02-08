
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    usuario = models.CharField(max_lenght=60, unique=True)
    adm_nome = models.CharField(max_lenght=60)
    senha_hash = models.CharField(128)
    is_admin = models.BooleanField(default=False)
    is_publisher = models.BooleanField(default=False)

    USERNAME_FIELD = 'usuario'
