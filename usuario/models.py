from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.conf import settings

class Usuario(AbstractBaseUser, PermissionsMixin):
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome']

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'usuario'
        verbose_name_plural = 'usuarios'
        permissions = [
            ('vizualizar_usuario', 'Pode visualizar usuario'),
    ]