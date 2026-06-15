from orders.gateways.order_gateway import OrderGateway
from orders.services.payment_factory import PaymentFactory


class OrderFacade:

    @staticmethod
    def finalizar_pedido(
        perfil,
        produto,
        adicionais,
        entrega,
        subtotal,
    ):

        pagamento = PaymentFactory.criar_pagamento(
            entrega.pagamento
        )

        pagamento_resultado = pagamento.pagar(
            perfil,
            subtotal + entrega.taxa,
        )

        pedido = {
            "cliente": {
                "nome": perfil.usuario.username,
            },
            "produto_nome": produto["nome"],
            "adicionais": adicionais,
            "entrega": entrega.tipo,
            "subtotal": subtotal,
            "taxa_entrega": entrega.taxa,
            "desconto": pagamento_resultado["desconto"],
            "valor_total": pagamento_resultado["valor_final"],
        }

        OrderGateway.criar({
            "usuario_id": perfil.usuario.id,
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

        return pedido, pagamento_resultado