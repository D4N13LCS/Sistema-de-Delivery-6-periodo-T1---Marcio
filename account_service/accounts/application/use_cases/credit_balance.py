from accounts.infrastructure.repositories.profile_repository import (
    ProfileRepository,
)


class CreditBalanceUseCase:

    def execute(self, user_id, value):
        profile = ProfileRepository.get_by_user_id(user_id=user_id)
        profile.balance += value

        return ProfileRepository.save(profile)