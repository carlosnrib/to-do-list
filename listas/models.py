from email.policy import default
from random import choices
from django.db import models

class Listas(models.Model):
    nome = models.CharField(max_length=256)
    def __str__(self) -> str:
        return self.nome

class Tarefa(models.Model):
    descricao = models.CharField(max_length=256)

    opcoes_prio = [
        (0, 'NENHUMA'),
        (1, 'ALTA'),
        (2, 'MÉDIA'),
        (3, 'BAIXA')
    ]
    prioridade = models.IntegerField(
        choices=opcoes_prio,
        default=0
    )

    data = models.DateField(null=True, blank=True)
    feita = models.BooleanField(default=False)
    lista = models.ForeignKey(Listas, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.descricao
