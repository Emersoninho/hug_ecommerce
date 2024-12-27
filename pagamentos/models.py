from django.db import models
from pedidos.models import Pedido

class Pagamento(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    metodo = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Pagamento do Pedido # {self.pedido.pk} - {self.metodo}'