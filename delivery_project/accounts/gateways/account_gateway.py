import requests


class AccountGateway:

    BASE_URL = "http://account-service:8003/api/accounts"

    @staticmethod
    def obter(usuario_id):

        try:
            response = requests.get(
                f"{AccountGateway.BASE_URL}/profile/{usuario_id}/",
                timeout=5,
            )

            response.raise_for_status()

            return response.json()

        except requests.exceptions.RequestException:
            return None

    @staticmethod
    def criar(usuario_id, saldo=200, endereco=""):

        try:
            response = requests.post(
                f"{AccountGateway.BASE_URL}/profile/create/",
                json={
                    "usuario_id": usuario_id,
                    "saldo": saldo,
                    "endereco": endereco,
                },
                timeout=5,
            )

            response.raise_for_status()

            return response.json()

        except requests.exceptions.RequestException:
            return None

    @staticmethod
    def atualizar(
        usuario_id,
        endereco="",
        numero_cartao="",
        nome_cartao="",
        validade_cartao="",
    ):
        try:
            response = requests.put(
                f"{AccountGateway.BASE_URL}/profile/{usuario_id}/update/",
                json={
                    "endereco": endereco,
                    "numero_cartao": numero_cartao,
                    "nome_cartao": nome_cartao,
                    "validade_cartao": validade_cartao,
                },
                timeout=5,
            )

            response.raise_for_status()
            return response.json()

        except requests.exceptions.RequestException:
            return None

    @staticmethod
    def excluir(usuario_id):

        try:
            response = requests.delete(
                f"{AccountGateway.BASE_URL}/profile/{usuario_id}/delete/",
                timeout=5,
            )

            response.raise_for_status()

            return response.json()

        except requests.exceptions.RequestException:
            return None

    @staticmethod
    def debitar(usuario_id, valor):

        try:
            response = requests.post(
                f"{AccountGateway.BASE_URL}/balance/debit/",
                json={
                    "usuario_id": usuario_id,
                    "valor": valor,
                },
                timeout=5,
            )

            response.raise_for_status()

            return response.json()

        except requests.exceptions.RequestException:
            return None

    @staticmethod
    def creditar(usuario_id, valor):

        try:
            response = requests.post(
                f"{AccountGateway.BASE_URL}/balance/credit/",
                json={
                    "usuario_id": usuario_id,
                    "valor": valor,
                },
                timeout=5,
            )

            response.raise_for_status()

            return response.json()

        except requests.exceptions.RequestException:
            return None