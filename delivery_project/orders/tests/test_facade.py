import pytest

from django.contrib.auth.models import User

from accounts.models import Perfil
from products.models import Produto

from orders.services.order_facade import (
    OrderFacade
)


@pytest.mark.django_db
def test_finalizar_pedido():

    user = User.objects.create_user(
        username="teste",
        password="123"
    )

    perfil = Perfil.objects.create(
        usuario=user,
        saldo=500
    )

    produto = Produto.objects.create(
        nome="X-Burger",
        preco=20,
        descricao="Teste",
        imagem="https://teste.com"
    )

    pedido, resultado = (
        OrderFacade.finalizar_pedido(
            perfil,
            produto,
            "",
            {
                "tipo": "normal",
                "taxa": 5,
                "pagamento": "pix"
            },
            20
        )
    )

    assert pedido.id is not None