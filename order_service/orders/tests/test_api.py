import json
import pytest

from django.test import Client


@pytest.mark.django_db
def test_create_order_api():

    client = Client()

    payload = {
        "usuario_id": 1,
        "produto_id": 10,
        "produto_nome": "X-Burger",
        "produto_preco": 25,
        "adicionais": "Queijo",
        "entrega": "normal",
        "pagamento": "pix",
        "subtotal": 25,
        "desconto": 0,
        "taxa_entrega": 5,
        "valor_total": 30,
    }

    response = client.post(
        "/api/orders/create/",
        data=json.dumps(payload),
        content_type="application/json",
    )

    assert response.status_code == 201


@pytest.mark.django_db
def test_list_orders_api():

    client = Client()

    response = client.get("/api/orders/")

    assert response.status_code == 200
    assert isinstance(response.json(), list)