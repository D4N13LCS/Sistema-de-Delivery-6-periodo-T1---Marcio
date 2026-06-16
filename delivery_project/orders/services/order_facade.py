from requests import RequestException

from orders.gateways.order_gateway import OrderGateway
from orders.services.payment_factory import PaymentFactory
from .payment_factory import WalletService

class OrderFacade:

    @staticmethod
    def finalizar_pedido(
        usuario_id,
        username,
        produto,
        adicionais,
        entrega,
        subtotal,
    ):

        pagamento = PaymentFactory.criar_pagamento(
            entrega.pagamento
        )

        pagamento_resultado = pagamento.pagar(
            usuario_id,
            subtotal + entrega.taxa,
        )

        pedido = {
            "cliente": {
                "nome": username,
            },
            "produto_nome": produto["nome"],
            "adicionais": adicionais,
            "entrega": entrega.tipo,
            "subtotal": subtotal,
            "taxa_entrega": entrega.taxa,
            "desconto": pagamento_resultado["desconto"],
            "valor_total": pagamento_resultado["valor_final"],
        }

        try:

            resultado = OrderGateway.criar({
                "usuario_id": usuario_id,
                "produto_id": produto["id"],
                "produto_nome": produto["nome"],
                "produto_preco": produto["preco"],
                "adicionais": adicionais,
                "entrega": entrega.tipo,
                "pagamento": entrega.pagamento,
                "subtotal": subtotal,
                "desconto": pagamento_resultado["desconto"],
                "taxa_entrega": entrega.taxa,
                "valor_total": pagamento_resultado["valor_final"],
            })
        
        except RequestException:

                WalletService.creditar(
                    usuario_id,
                    pagamento_resultado["valor_final"],
                )

                raise ValueError(
                    "Não foi possível concluir o pedido. "
                    "Seu saldo foi restaurado automaticamente."
                )
        return pedido, pagamento_resultado
               