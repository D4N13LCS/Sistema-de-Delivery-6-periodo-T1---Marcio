from orders.models import Pedido
from orders.services.payment_factory import PaymentFactory


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
            entrega["pagamento"]
        )

        pagamento_resultado = pagamento.pagar(
            perfil,
            subtotal + entrega["taxa"]
        )

        pedido = Pedido.objects.create(

            usuario=perfil.usuario,

            produto=produto,

            adicionais=adicionais,

            entrega=entrega["tipo"],

            pagamento=entrega["pagamento"],

            subtotal=subtotal,

            desconto=pagamento_resultado["desconto"],

            taxa_entrega=entrega["taxa"],

            valor_total=pagamento_resultado["valor_final"]
        )

        return pedido, pagamento_resultado