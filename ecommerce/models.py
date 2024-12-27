from django.db import models

class Ecommerce(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.nome

class ConfiguracaoEcommerce(models.Model):
    tema = models.CharField(max_length=255)
    cor_principal = models.CharField(max_length=20)
    cor_secundaria = models.CharField(max_length=20)
    logo = models.ImageField(upload_to='ecommerce', blank=True, null=True)

    def __str__(self):
        return 'Configurações do Ecommerce'    