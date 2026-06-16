from accounts.gateways.account_gateway import AccountGateway


def perfil_context(request):
    if request.user.is_authenticated:
        perfil = AccountGateway.obter(request.user.id)

        if perfil is None:
            perfil = {}

        return {
            "perfil": perfil
        }

    return {
        "perfil": {}
    }