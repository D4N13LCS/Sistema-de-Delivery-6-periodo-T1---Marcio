from django.db import models

class Perfil(models.Model):

    usuario_id = models.IntegerField(unique=True)

    endereco = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    saldo = models.FloatField(default=200)

    cartao_cadastrado = models.BooleanField(default=False)

    numero_cartao = models.CharField(
        max_length=16,
        blank=True,
        null=True
    )

    nome_cartao = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    validade_cartao = models.CharField(
        max_length=5,
        blank=True,
        null=True
    )

    def __str__(self):
        return f"Perfil do usuário {self.usuario_id}"