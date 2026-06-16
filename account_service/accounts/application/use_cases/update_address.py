from accounts.models import Perfil


class UpdateAddressUseCase:

    def execute(self, usuario_id, endereco):
        perfil = Perfil.objects.get(usuario_id=usuario_id)
        perfil.endereco = endereco
        perfil.save()

        return perfil