from django.db import models
from produtos.models import Produto
from django.conf import settings

class Avaliacao(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    avaliacao = models.IntegerField(default=0)
    comentario = models.TextField()

    def __str__(self):
        return f'Avaliação do Produto {self.produto.nome} - {self.usuario.username}'