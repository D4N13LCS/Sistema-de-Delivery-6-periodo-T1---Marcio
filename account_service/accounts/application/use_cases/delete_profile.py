from accounts.infrastructure.repositories.profile_repository import (
    ProfileRepository,
)

class DeleteProfileUseCase:

    def execute(self, user_id):
        profile = ProfileRepository.get_by_user_id(user_id)
        ProfileRepository.delete(profile)