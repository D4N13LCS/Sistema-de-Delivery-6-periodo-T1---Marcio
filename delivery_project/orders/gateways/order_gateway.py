import requests
from delivery_project.settings import ORDER_SERVICE_URL

class OrderGateway:

    # BASE_URL = "http://order-service:8002/api/orders"
    BASE_URL = f"{ORDER_SERVICE_URL}/api/orders"
    @staticmethod
    def listar():
        try:
            response = requests.get(
                f"{OrderGateway.BASE_URL}/",
                timeout=5,  # importante para não ficar travado
            )
            response.raise_for_status()
            return response.json()

        except requests.exceptions.RequestException:
            return []

    @staticmethod
    def criar(payload):
        try:
            response = requests.post(
                f"{OrderGateway.BASE_URL}/create/",
                json=payload,
                timeout=5,
            )
            response.raise_for_status()
            return response.json()

        except requests.exceptions.RequestException:
            raise