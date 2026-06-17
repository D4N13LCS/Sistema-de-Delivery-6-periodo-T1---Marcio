from accounts.infrastructure.repositories.profile_repository import (
    ProfileRepository,
)


class GetProfileUseCase:

    def execute(self, user_id):
        profile, _ = ProfileRepository.get_or_create(
            user_id=user_id,
            balance=200,
        )

        return profile