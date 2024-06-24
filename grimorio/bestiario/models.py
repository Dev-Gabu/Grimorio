from django.db import models
from bestiario.consts import OPCOES_ELEMENTO

class Criatura(models.Model):
    nome = models.CharField(max_length=100)
    rank = models.CharField(max_length=1)
    descricao = models.TextField(blank=True, null=True)
    foto = models.ImageField(blank=True, null=True, upload_to='bestiario/fotos')
    experiencia = models.SmallIntegerField(default=0)
    doragos = models.SmallIntegerField(default=0)
    elemento = models.SmallIntegerField(choices=OPCOES_ELEMENTO,default=0)

    def __str__(self):
        return '{0} - Rank {1}'.format(
            self.nome,
            self.rank
        )

    def get_nome_elemento(self):
        for codigo, nome in OPCOES_ELEMENTO:
            if self.elemento == codigo:
                return nome
        return None