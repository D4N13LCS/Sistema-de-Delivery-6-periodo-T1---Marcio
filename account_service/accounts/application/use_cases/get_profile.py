from accounts.models import Perfil


class GetProfileUseCase:

    def execute(self, usuario_id):
        perfil, _ = Perfil.objects.get_or_create(
            usuario_id=usuario_id,
            defaults={"saldo": 200},
        )

        return perfil