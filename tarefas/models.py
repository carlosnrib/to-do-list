from email.policy import default
from random import choice
from django.db import models

class Tarefas(models.Model):
    descricao = models.CharField(max_length=256)

    opcoes_prio = [
        (0, 'NENHUMA'),
        (1, 'ALTA'),
        (2, 'MÉDIA'),
        (3, 'BAIXA')
    ]
    prioridade = models.IntegerField(
        max_length=1,
        choices=opcoes_prio,
        default=0
    )

    data = models.DateField(null=True)
    feita = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.descricao


