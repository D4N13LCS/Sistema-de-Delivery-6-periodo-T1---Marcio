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

    clientes = [
        {"nome": "Carlos", "saldo": 150},
        {"nome": "Marina", "saldo": 80},
        {"nome": "Fernanda", "saldo": 250},
        {"nome": "Lucas", "saldo": 40},
    ]

    for cliente in clientes:

        usuario, created = User.objects.get_or_create(
            username=cliente["nome"]
        )

        if created:
            usuario.set_password("123")
            usuario.save()

        perfil = AccountGateway.obter(usuario.id)

        if perfil is None:

            AccountGateway.criar(
                usuario_id=usuario.id,
                saldo=cliente["saldo"],
                endereco="Endereço padrão",
            )

        else:

            # atualiza apenas o endereço
            AccountGateway.atualizar(
                usuario_id=usuario.id,
                endereco="Endereço padrão",
            )

            # atualiza o saldo usando o endpoint próprio
            saldo_atual = perfil["saldo"]
            saldo_desejado = cliente["saldo"]

            diferenca = saldo_desejado - saldo_atual

            if diferenca > 0:
                AccountGateway.creditar(
                    usuario.id,
                    diferenca,
                )

            elif diferenca < 0:
                AccountGateway.debitar(
                    usuario.id,
                    abs(diferenca),
                )

    print("Seed executada com sucesso!")


if __name__ == "__main__":
    run()