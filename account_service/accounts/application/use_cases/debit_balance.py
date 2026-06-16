from accounts.models import Perfil


class DebitBalanceUseCase:

    def execute(self, usuario_id, valor):
        perfil = Perfil.objects.get(usuario_id=usuario_id)

        if perfil.saldo < valor:
            raise ValueError("Saldo insuficiente")

        perfil.saldo -= valor
        perfil.save()

        return perfil