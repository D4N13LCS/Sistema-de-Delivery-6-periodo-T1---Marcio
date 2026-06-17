from django.test import TestCase

from accounts.application.use_cases.create_profile import CreateProfileUseCase
from accounts.models import Profile


class CreateProfileUseCaseTest(TestCase):

    def test_should_create_profile(self):
        profile, created = CreateProfileUseCase.execute(
            user_id=1,
            balance=300,
            address="Main Street",
        )

        self.assertTrue(created)
        self.assertEqual(profile.user_id, 1)
        self.assertEqual(profile.balance, 300)
        self.assertEqual(profile.address, "Main Street")

    def test_should_not_duplicate_existing_profile(self):
        Profile.objects.create(
            user_id=1,
            balance=100,
            address="Old Address",
        )

        profile, created = CreateProfileUseCase.execute(
            user_id=1,
        )

        self.assertFalse(created)
        self.assertEqual(Profile.objects.count(), 1)
        self.assertEqual(profile.user_id, 1)
    
    def test_should_create_profile_with_default_values(self):
        profile, created = CreateProfileUseCase().execute(
            user_id=100
        )

        self.assertTrue(created)
        self.assertEqual(profile.balance, 200)
        self.assertEqual(profile.address, "")