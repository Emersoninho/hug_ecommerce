from django.db import models

class Cupom(models.Model):
    nome = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    validade = models.DateField()

    def __str__(self):
        return f'Cupom {self.nome} - {self.valor}'