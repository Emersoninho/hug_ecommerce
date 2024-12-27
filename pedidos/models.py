from django.db import models
from carrinho.models import Carrinho
from produtos.models import Produto

class Pedido(models.Model):
    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    itens = models.ManyToManyField(Carrinho)

    def __str__(self):
        return f'Pedido # {self.pk} - {self.usuario.username}'

class PedidoItem(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=1)

    def __str__(self):
        return f'Item do Pedido # {self.pedido.pk} - {self.produto.nome}'