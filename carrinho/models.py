from django.db import models
from produtos.models import Produto
from django.conf import settings

class Carrinho(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=1)

    def __str__(self):
        return f'Carrinho de {self.usuario.username} - {self.produto.nome}'