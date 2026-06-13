from django.db import models
from django.contrib.auth.models import User
from products.models import Produto

# Create your models here.
class Pedido(models.Model):

    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    produto_id = models.IntegerField(null=True)

    produto_nome = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    produto_preco = models.FloatField(null=True)

    adicionais = models.TextField()

    entrega = models.CharField(max_length=30)

    pagamento = models.CharField(max_length=30)

    subtotal = models.FloatField()

    desconto = models.FloatField()

    taxa_entrega = models.FloatField()

    valor_total = models.FloatField()

    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Pedido #{self.id}'