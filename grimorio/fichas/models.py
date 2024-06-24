from django.db import models
from fichas.consts import OPCOES_CLASSE, OPCOES_ELEMENTO

class Ficha(models.Model):
    nome = models.CharField(max_length=100)
    nivel = models.SmallIntegerField(default=1)
    experiencia = models.SmallIntegerField(default=0)
    doragos = models.SmallIntegerField(default=0)
    classe = models.SmallIntegerField(choices=OPCOES_CLASSE,default=0)
    elemento = models.SmallIntegerField(choices=OPCOES_ELEMENTO,default=0)
    foto = models.ImageField(blank=True, null=True, upload_to='fichas/fotos')
    equipamento = models.TextField(blank=True, null=True)
    feiticos = models.TextField(blank=True, null=True)

    def __str__(self):
        return '{0} - {1}'.format(
            self.nome,
            self.get_classe_display()
        )

    def get_nome_classe(self):
        for codigo, nome in OPCOES_CLASSE:
            if self.classe == codigo:
                return nome
        return None

    def get_nome_elemento(self):
        for codigo, nome in OPCOES_ELEMENTO:
            if self.elemento == codigo:
                return nome
        return None