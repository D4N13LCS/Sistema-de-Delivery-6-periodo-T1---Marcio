import pytest

from orders.application.use_cases.create_order import CreateOrderUseCase
from orders.models import Pedido


@pytest.mark.django_db
def test_create_order_use_case():

    data = {
        "usuario_id": 1,
        "produto_id": 10,
        "produto_nome": "X-Burger",
        "produto_preco": 25.0,
        "adicionais": "Queijo, Bacon",
        "entrega": "normal",
        "pagamento": "pix",
        "subtotal": 30.0,
        "desconto": 2.0,
        "taxa_entrega": 5.0,
        "valor_total": 33.0,
    }

    pedido = CreateOrderUseCase().execute(data)

    assert pedido.id is not None
    assert Pedido.objects.count() == 1

    assert pedido.usuario_id == 1
    assert pedido.produto_nome == "X-Burger"
    assert pedido.pagamento == "pix"
    assert pedido.valor_total == 33.0