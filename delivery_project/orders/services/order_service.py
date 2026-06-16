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
    OrderFacade
)

from .dtos import DeliveryData

from orders.gateways.order_gateway import OrderGateway

class OrderService:

    @staticmethod
    def _montar_lanche(produto, adicionais_selecionados):
        lanche = Lanche(
            produto["nome"],
            produto["preco"],
        )

        adicionais = []

        if "queijo" in adicionais_selecionados:
            lanche = ExtraQueijo(lanche)
            adicionais.append("Queijo")

        if "bacon" in adicionais_selecionados:
            lanche = Bacon(lanche)
            adicionais.append("Bacon")

        if "catupiry" in adicionais_selecionados:
            lanche = Catupiry(lanche)
            adicionais.append("Catupiry")

        return lanche, adicionais

    @staticmethod
    def _obter_strategy(tipo_entrega):
        if tipo_entrega == "expressa":
            return EntregaExpressa()

        return EntregaNormal()

    @staticmethod
    def criar_pedido(
        usuario_id,
        username,
        produto,
        tipo_entrega,
        tipo_pagamento,
        adicionais_selecionados,
    ):
        lanche, adicionais = OrderService._montar_lanche(
            produto,
            adicionais_selecionados,
        )

        subtotal = lanche.preco()

        strategy = OrderService._obter_strategy(
            tipo_entrega
        )

        taxa = strategy.calcular(subtotal)

        entrega = DeliveryData(
            tipo=tipo_entrega,
            taxa=taxa,
            pagamento=tipo_pagamento,
        )

        pedido, resultado = OrderFacade.finalizar_pedido(
            usuario_id=usuario_id,
            username=username,
            produto=produto,
            adicionais=", ".join(adicionais),
            entrega=entrega,
            subtotal=subtotal,
        )

        return pedido, resultado
