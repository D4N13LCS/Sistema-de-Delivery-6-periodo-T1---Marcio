from django.http import JsonResponse

from products.application.use_cases.list_products import (
    ListProductsUseCase
)

from products.infrastructure.repositories.django_product_repository import (
    DjangoProductRepository
)


def list_products(request):

    repository = DjangoProductRepository()

    use_case = ListProductsUseCase(repository)

    produtos = use_case.execute()

    data = [
        {
            "id": p.id,
            "nome": p.nome,
            "preco": float(p.preco)
        }
        for p in produtos
    ]

    return JsonResponse(data, safe=False)