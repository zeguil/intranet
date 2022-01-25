from django.db import models

class Email(models.Model):

    email = models.CharField()
    responsavel = models.CharField()

    def __str__(self):
        return f'<Email: {self.id}>'