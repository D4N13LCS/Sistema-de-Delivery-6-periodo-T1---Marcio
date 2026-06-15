import requests


class OrderGateway:

    BASE_URL = "http://order-service:8002/api/orders"

    @staticmethod
    def listar():
        response = requests.get(
            f"{OrderGateway.BASE_URL}/"
        )
        response.raise_for_status()
        return response.json()

    @staticmethod
    def criar(payload):
        response = requests.post(
            f"{OrderGateway.BASE_URL}/create/",
            json=payload,
        )
        response.raise_for_status()
        return response.json()