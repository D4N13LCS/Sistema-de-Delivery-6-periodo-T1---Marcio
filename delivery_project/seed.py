import os
import django

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "delivery_project.settings"
)

django.setup()

from django.contrib.auth.models import User
from accounts.gateways.account_gateway import AccountGateway


def run():

    clients = [
        {"name": "Carlos", "balance": 150},
        {"name": "Marina", "balance": 80},
        {"name": "Fernanda", "balance": 250},
        {"name": "Lucas", "balance": 40},
    ]

    for client in clients:

        user, created = User.objects.get_or_create(
            username=client["name"]
        )

        if created:
            user.set_password("123")
            user.save()

        profile = AccountGateway.get_profile(user.id)

        if profile is None:

            AccountGateway.create_profile(
                user_id=user.id,
                balance=client["balance"],
                address="default address",
            )

        else:

            # update address only
            AccountGateway.update_profile(
                user_id=user.id,
                address="default address",
            )

            # atualiza o saldo usando o endpoint próprio
            current_balance = profile["balance"]
            new_balance_value = client["balance"]

            difference = new_balance_value - current_balance

            if difference > 0:
                AccountGateway.credit_balance(
                    user.id,
                    difference,
                )

            elif difference < 0:
                AccountGateway.debit_balance(
                    user.id,
                    abs(difference),
                )

    print("Seed successfully executed!")


if __name__ == "__main__":
    run()