from django.db import models
from fichas.consts import OPCOES_SISTEMA

class Ficha(models.Model):
    nome = models.CharField(max_length=100)
    sistema = models.SmallIntegerField(choices=OPCOES_SISTEMA)
    foto = models.ImageField(blank=True, null=True, upload_to='fichas/fotos')

    def __str__(self):
        return '{0} - {1}'.format(
            self.nome,
            self.get_sistema_display()
        )

    def get_nome_sistema(self):
        for codigo, nome in OPCOES_SISTEMA:
            if self.sistema == codigo:
                return nome
        return None