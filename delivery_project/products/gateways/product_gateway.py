import logging
import requests

logger = logging.getLogger(__name__)

class ProductGateway:
    BASE_URL = "http://product-service:8001/api/products/"

    @classmethod
    def listar(cls):
        try:
            response = requests.get(
                cls.BASE_URL,
                timeout=3
            )

            response.raise_for_status()

            return response.json()

        except requests.exceptions.RequestException as excecao:
            logger.error(f"Erro ao acessar Product Service: {excecao}")
            return []
        
    @classmethod
    def buscar_por_id(cls, produto_id):
        produtos = cls.listar()

        for produto in produtos:
            if produto["id"] == int(produto_id):
                return produto

        return None