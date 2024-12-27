from django.db import models
from produtos.models import Produto

class Carrinho(models.Model):
    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=1)

    def __str__(self):
        return f'Carrinho de {self.usuario.username} - {self.produto.nome}'