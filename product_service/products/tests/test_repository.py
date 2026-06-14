import pytest

from products.infrastructure.repositories.django_product_repository import (
    DjangoProductRepository,
)
from products.models import Produto


@pytest.mark.django_db
def test_repository_lista_produtos():

    Produto.objects.create(
        nome="X-Burger",
        preco=20,
        descricao="Teste",
        imagem="https://teste.com"
    )

    repository = DjangoProductRepository()

    produtos = repository.list_all()

    assert len(produtos) == 1
    assert produtos[0].nome == "X-Burger"