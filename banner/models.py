from django.db import models
from uuid import uuid4


class Banner(models.Model):

    titulo = models.CharField(max_length=60)
    conteudo = models.TextField()
    hasPage = models.BooleanField(default=False)
    image = models.ImageField(upload_to='banner', blank=True, null=True )
    data_pub = models.DateField(auto_now_add=True)
    state = models.IntegerField(default=0)

    def __str__(self):
        return f'<Banner: {self.titulo}>'