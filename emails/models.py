from django.db import models

class Email(models.Model):

    email = models.CharField(max_length=80)
    responsavel = models.CharField(max_length=80)

    def __str__(self):
        return f'<Email: {self.id}>'