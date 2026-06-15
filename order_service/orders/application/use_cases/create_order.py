from orders.models import Pedido


class CreateOrderUseCase:

    def execute(self, data):
        pedido = Pedido.objects.create(
            usuario_id=data["usuario_id"],
            produto_id=data["produto_id"],
            produto_nome=data["produto_nome"],
            produto_preco=data["produto_preco"],
            adicionais=data["adicionais"],
            entrega=data["entrega"],
            pagamento=data["pagamento"],
            subtotal=data["subtotal"],
            desconto=data["desconto"],
            taxa_entrega=data["taxa_entrega"],
            valor_total=data["valor_total"],
        )

        return pedido