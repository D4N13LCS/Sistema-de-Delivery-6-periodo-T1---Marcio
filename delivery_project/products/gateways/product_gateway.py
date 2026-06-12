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

        except requests.exceptions.RequestException as e:
            logger.error(f"Erro ao acessar Product Service: {e}")
            return []