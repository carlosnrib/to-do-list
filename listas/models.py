from django.db import models

class Listas(models.Model):
    nome = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.nome

