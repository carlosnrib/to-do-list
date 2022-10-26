from email.policy import default
from random import choices
from django.db import models

# Criacao dos modelos

# Modelo das Listas
class Listas(models.Model):
    # Atributos do modelo
    nome = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.nome

# Modelo das Tarefas
class Tarefa(models.Model):
    # Atributos do modelo
    descricao = models.CharField(max_length=256)
    data = models.DateField(null=True, blank=True)
    feita = models.BooleanField(default=False)

    # Opcoes que o atributo "prioridade" pode ter
    opcoes_prio = [
        (0, 'NENHUMA'),
        (1, 'BAIXA'),
        (2, 'MÉDIA'),
        (3, 'ALTA')
    ]
    prioridade = models.IntegerField(
        choices=opcoes_prio,
        default=0
    )

    # Ligacao entre uma tarefa e a lista que a pertence
    lista = models.ForeignKey(Listas, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.descricao
