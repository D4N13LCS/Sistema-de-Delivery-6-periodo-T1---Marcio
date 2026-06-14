from unittest.mock import Mock

from products.application.use_cases.list_products import (
    ListProductsUseCase,
)


def test_list_products_use_case():
    repository = Mock()

    repository.list_all.return_value = [
        {"id": 1, "nome": "X-Burger"}
    ]

    use_case = ListProductsUseCase(repository)

    resultado = use_case.execute()

    assert len(resultado) == 1
    repository.list_all.assert_called_once()