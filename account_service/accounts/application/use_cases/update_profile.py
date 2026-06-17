from accounts.infrastructure.repositories.profile_repository import (
    ProfileRepository,
)


class UpdateProfileUseCase:

    def execute(
        self,
        user_id,
        address=None,
        card_number=None,
        card_name=None,
        card_expiration=None,
    ):
        profile = ProfileRepository.get_by_user_id(user_id)

        if address is not None:
            profile.address = address

        if card_number is not None:
            profile.card_number = card_number

        if card_name is not None:
            profile.card_name = card_name

        if card_expiration is not None:
            profile.card_expiration = card_expiration

        profile.card_registered = bool(profile.card_number)

        return ProfileRepository.save(profile)