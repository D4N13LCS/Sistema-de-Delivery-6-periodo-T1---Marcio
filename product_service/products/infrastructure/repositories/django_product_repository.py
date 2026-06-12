from products.models import Produto
from products.domain.entities.product import Product


class DjangoProductRepository:

    def list_all(self):

        produtos = Produto.objects.all()

        return [
            Product(
                p.id,
                p.nome,
                p.preco,
                p.descricao,
                p.imagem
            )
            for p in produtos
        ]