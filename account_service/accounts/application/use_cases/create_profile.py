from accounts.infrastructure.repositories.profile_repository import (
    ProfileRepository,
)


class CreateProfileUseCase:

    @staticmethod
    def execute(
        user_id,
        balance=200,
        address="",
    ):
        profile, created = ProfileRepository.get_or_create(
            user_id=user_id,
            balance=balance,
            address=address,
        )

        print(created)
        print(profile.balance)
        print(profile.address)

        return profile, created