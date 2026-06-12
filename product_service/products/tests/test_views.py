import pytest

from products.models import Produto


@pytest.mark.django_db
def test_home_paginada(client):

    for i in range(15):

        Produto.objects.create(
            nome=f"Produto {i}",
            preco=10,
            descricao="Teste",
            imagem="https://teste.com"
        )

    response = client.get("/")

    assert response.status_code == 200

    assert len(
        response.context["produtos"]
    ) <= 6