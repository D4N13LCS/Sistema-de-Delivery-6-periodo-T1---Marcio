from orders.models import Pedido
from orders.domain.entities.order import Order


class DjangoOrderRepository:

    def list_all(self):

        pedidos = Pedido.objects.all().order_by("-criado_em")

        return [
            Order(
                id=p.id,
                usuario_id=p.usuario_id,
                produto_id=p.produto_id,
                produto_nome=p.produto_nome,
                produto_preco=p.produto_preco,
                adicionais=p.adicionais,
                entrega=p.entrega,
                pagamento=p.pagamento,
                subtotal=p.subtotal,
                desconto=p.desconto,
                taxa_entrega=p.taxa_entrega,
                valor_total=p.valor_total,
                criado_em=p.criado_em,
            )
            for p in pedidos
        ]