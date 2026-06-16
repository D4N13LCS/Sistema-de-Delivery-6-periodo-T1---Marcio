from accounts.models import Perfil


class CreateProfileUseCase:

    @staticmethod
    def execute(
        usuario_id,
        saldo=200,
        endereco="",
    ):
        perfil, created = Perfil.objects.get_or_create(
            usuario_id=usuario_id,
            defaults={
                "saldo": saldo,
                "endereco": endereco,
            },
        )

        return perfil, created