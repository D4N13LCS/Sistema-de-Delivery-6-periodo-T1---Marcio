from accounts.models import Perfil


class CreditBalanceUseCase:

    def execute(self, usuario_id, valor):
        perfil = Perfil.objects.get(usuario_id=usuario_id)
        perfil.saldo += valor
        perfil.save()

        return perfil