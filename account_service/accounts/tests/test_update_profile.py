from django.test import TestCase

from accounts.application.use_cases.update_profile import UpdateProfileUseCase
from accounts.models import Profile


class UpdateProfileUseCaseTest(TestCase):

    def test_should_update_profile_information(self):
        Profile.objects.create(
            user_id=1,
            address="Old Address",
        )

        profile = UpdateProfileUseCase().execute(
            user_id=1,
            address="New Address",
            card_number="1234123412341234",
            card_name="John Doe",
            card_expiration="12/30",
        )

        self.assertEqual(profile.address, "New Address")
        self.assertEqual(profile.card_number, "1234123412341234")
        self.assertEqual(profile.card_name, "John Doe")
        self.assertEqual(profile.card_expiration, "12/30")
        self.assertTrue(profile.card_registered)
    
    def test_should_update_only_address(self):
        Profile.objects.create(
            user_id=5,
            address="Old",
            balance=100,
        )

        profile = UpdateProfileUseCase().execute(
            user_id=5,
            address="New",
        )

        self.assertEqual(profile.address, "New")