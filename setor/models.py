from django.db import models
from uuid import uuid4
from funcionario.models import Funcionario
from ramal.models import Ramal
# from corporativo.models import Corporativo

class Setor(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    set_nome = models.CharField(max_length=60, index=True)
    state = models.IntegerField(default=0)
    ramal = models.ForeignKey(Ramal, on_delete=models.CASCADE)
    func = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    #corporativo = models.ManyToManyField(Corporativo)

    def __str__(self):
        return self.set_nome