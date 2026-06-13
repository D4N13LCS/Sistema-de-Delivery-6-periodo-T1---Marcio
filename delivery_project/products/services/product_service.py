from products.gateways.product_gateway import ProductGateway

class ProductService:

    @staticmethod
    def listar():
        return ProductGateway.listar()

    @staticmethod
    def buscar_por_id(produto_id):
        return ProductGateway.buscar_por_id(produto_id)