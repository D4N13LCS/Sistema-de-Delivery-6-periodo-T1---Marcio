import pytest

from products.models import Produto

@pytest.mark.django_db
def test_listagem_sem_produtos(client):
    response = client.get("/api/products/")

    assert response.status_code == 200
    assert response.json() == []

@pytest.mark.django_db
def test_api_lista_produtos(client):

    Produto.objects.create(
        nome="X-Burger",
        preco=20,
        descricao="Teste",
        imagem="https://teste.com"
    )

    response = client.get("/api/products/")

    assert response.status_code == 200

    data = response.json()

    assert len(data) == 1
    assert data[0]["nome"] == "X-Burger"