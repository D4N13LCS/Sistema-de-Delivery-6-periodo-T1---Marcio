import requests
from delivery_project.settings import ACCOUNT_SERVICE_URL

class AccountGateway:
    BASE_URL = f"{ACCOUNT_SERVICE_URL}/api/accounts"

    @staticmethod
    def get_profile(user_id):

        try:
            response = requests.get(
                f"{AccountGateway.BASE_URL}/profile/{user_id}/",
                timeout=5,
            )

            response.raise_for_status()

            return response.json()

        except requests.exceptions.RequestException:
            return None

    @staticmethod
    def create_profile(user_id, balance=200, address=""):

        try:
            response = requests.post(
                f"{AccountGateway.BASE_URL}/profile/create/",
                json={
                    "user_id": user_id,
                    "balance": balance,
                    "address": address,
                },
                timeout=5,
            )

            response.raise_for_status()

            return response.json()

        except requests.exceptions.RequestException:
            return None

    @staticmethod
    def update_profile(
        user_id,
        address="",
        card_number="",
        card_name="",
        card_expiration="",
    ):
        try:
            response = requests.put(
                f"{AccountGateway.BASE_URL}/profile/{user_id}/update/",
                json={
                    "address": address,
                    "card_number": card_number,
                    "card_name": card_name,
                    "card_expiration": card_expiration,
                },
                timeout=5,
            )

            response.raise_for_status()
            return response.json()

        except requests.exceptions.RequestException:
            return None

    @staticmethod
    def delete_profile(user_id):

        try:
            response = requests.delete(
                f"{AccountGateway.BASE_URL}/profile/{user_id}/delete/",
                timeout=5,
            )

            response.raise_for_status()

            return response.json()

        except requests.exceptions.RequestException:
            return None

    @staticmethod
    def debit_balance(user_id, value):

        try:
            response = requests.post(
                f"{AccountGateway.BASE_URL}/balance/debit/",
                json={
                    "user_id": user_id,
                    "value": value,
                },
                timeout=5,
            )

            response.raise_for_status()

            return response.json()

        except requests.exceptions.RequestException:
            return None

    @staticmethod
    def credit_balance(user_id, value):

        try:
            response = requests.post(
                f"{AccountGateway.BASE_URL}/balance/credit/",
                json={
                    "user_id": user_id,
                    "value": value,
                },
                timeout=5,
            )

            response.raise_for_status()

            return response.json()

        except requests.exceptions.RequestException:
            return None