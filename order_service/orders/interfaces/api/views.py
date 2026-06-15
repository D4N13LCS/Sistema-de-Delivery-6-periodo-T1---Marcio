import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone

from orders.application.use_cases.create_order import CreateOrderUseCase

from orders.application.use_cases.list_orders import (
    ListOrdersUseCase,
)

from orders.infrastructure.repositories.django_order_repository import (
    DjangoOrderRepository,
)


def list_orders(request):
    repository = DjangoOrderRepository()

    use_case = ListOrdersUseCase(repository)

    pedidos = use_case.execute()

    data = [
        {
            "id": p.id,
            "usuario_id": p.usuario_id,
            "produto_id": p.produto_id,
            "produto_nome": p.produto_nome,
            "produto_preco": p.produto_preco,
            "adicionais": p.adicionais,
            "entrega": p.entrega,
            "pagamento": p.pagamento,
            "subtotal": p.subtotal,
            "desconto": p.desconto,
            "taxa_entrega": p.taxa_entrega,
            "valor_total": p.valor_total,
            "criado_em": timezone.localtime(p.criado_em).strftime("%d/%m/%Y %H:%M") if p.criado_em else None,
        }
        for p in pedidos
    ]

    return JsonResponse(data, safe=False)

@csrf_exempt
def create_order(request):

    if request.method != "POST":
        return JsonResponse(
            {"error": "Method not allowed"},
            status=405
        )

    data = json.loads(request.body)

    pedido = CreateOrderUseCase().execute(data)

    return JsonResponse(
        {
            "id": pedido.id,
            "status": "created",
        },
        status=201,
    )