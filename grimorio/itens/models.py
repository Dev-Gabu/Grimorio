from django.db import models
from itens.consts import OPCOES_RARIDADE

class Item(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=1000)
    durabilidade = models.IntegerField()
    raridade = models.SmallIntegerField(choices=OPCOES_RARIDADE)
    foto = models.ImageField(blank=True, null=True, upload_to='itens/fotos')

    def __str__(self):
        return '{0} - {2} ({1})'.format(
            self.nome,
            self.durabilidade,
            self.get_raridade_display()
        )

    def get_nome_raridade(self):
        for codigo, nome in OPCOES_RARIDADE:
            if self.raridade == codigo:
                return nome
        return None