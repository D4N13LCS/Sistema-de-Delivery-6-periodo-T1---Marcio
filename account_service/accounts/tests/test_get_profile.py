from django.test import TestCase

from accounts.application.use_cases.get_profile import GetProfileUseCase
from accounts.models import Profile


class GetProfileUseCaseTest(TestCase):

    def test_should_return_existing_profile(self):
        Profile.objects.create(
            user_id=10,
            balance=500,
        )

        profile = GetProfileUseCase().execute(10)

        self.assertEqual(profile.user_id, 10)
        self.assertEqual(profile.balance, 500)

    def test_should_create_default_profile_if_missing(self):
        profile = GetProfileUseCase().execute(20)

        self.assertEqual(profile.user_id, 20)
        self.assertEqual(profile.balance, 200)