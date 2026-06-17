from accounts.infrastructure.repositories.profile_repository import (
    ProfileRepository,
)

class DebitBalanceUseCase:

    def execute(self, user_id, value):

        profile = ProfileRepository.get_by_user_id(user_id)

        if profile.balance < value:
            raise ValueError("Insufficient balance")

        profile.balance -= value

        return ProfileRepository.save(profile)