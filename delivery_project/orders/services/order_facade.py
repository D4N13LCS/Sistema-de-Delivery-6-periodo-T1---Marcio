from orders.models import Pedido
from orders.services.payment_factory import PaymentFactory
from orders.services.dtos import DeliveryData

class OrderFacade:

    @staticmethod
    def finalizar_pedido(
        perfil,
        produto,
        adicionais,
        entrega,
        subtotal
    ):

        pagamento = PaymentFactory.criar_pagamento(
            entrega.pagamento
        )

        pagamento_resultado = pagamento.pagar(
            perfil,
            subtotal + entrega.taxa
        )

        pedido = Pedido.objects.create(

            usuario=perfil.usuario,

            produto_id=produto["id"],
            produto_nome=produto["nome"],
            produto_preco=produto["preco"],

            adicionais=adicionais,

            entrega=entrega.tipo,

            pagamento=entrega.pagamento,

            subtotal=subtotal,

            desconto=pagamento_resultado["desconto"],

            taxa_entrega=entrega.taxa,

            valor_total=pagamento_resultado["valor_final"]
        )

        return pedido, pagamento_resultado