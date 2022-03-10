from django.db import models
from users.models import User
from datetime import datetime
from uuid import uuid4


class Informativo(models.Model):

    titulo = models.CharField(max_length=60)
    link = models.URLField()#verify_exists=True
    image = models.ImageField(upload_to='informativos', blank=True, null=True )
    data_pub = models.DateField(auto_now_add=True)
    state = models.IntegerField(default=0)
    admin_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Informativo: {self.titulo}'

    