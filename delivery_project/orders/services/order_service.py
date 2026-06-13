from orders.services.decorators import (
    Lanche,
    ExtraQueijo,
    Bacon,
    Catupiry,
)
from orders.services.delivery_strategy import (
    EntregaNormal,
    EntregaExpressa,
)
from orders.services.order_facade import (
    OrderFacade,
    DeliveryData,
)


class OrderService:

    @staticmethod
    def criar_pedido(
        perfil,
        produto,
        request
    ):
        lanche = Lanche(
            produto["nome"],
            produto["preco"]
        )

        adicionais = []

        if "queijo" in request.POST:
            lanche = ExtraQueijo(lanche)
            adicionais.append("Queijo")

        if "bacon" in request.POST:
            lanche = Bacon(lanche)
            adicionais.append("Bacon")

        if "catupiry" in request.POST:
            lanche = Catupiry(lanche)
            adicionais.append("Catupiry")

        subtotal = lanche.preco()

        strategy = (
            EntregaExpressa()
            if request.POST["entrega"] == "expressa"
            else EntregaNormal()
        )

        taxa = strategy.calcular(subtotal)

        entrega = DeliveryData(
            tipo=request.POST["entrega"],
            taxa=taxa,
            pagamento=request.POST["pagamento"],
        )

        return OrderFacade.finalizar_pedido(
            perfil=perfil,
            produto=produto,
            adicionais=", ".join(adicionais),
            entrega=entrega,
            subtotal=subtotal,
        )