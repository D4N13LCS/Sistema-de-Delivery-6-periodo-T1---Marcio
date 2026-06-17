from django.test import TestCase

from accounts.application.use_cases.delete_profile import DeleteProfileUseCase
from accounts.models import Profile


class DeleteProfileUseCaseTest(TestCase):

    def test_should_delete_existing_profile(self):
        Profile.objects.create(
            user_id=1,
            balance=100,
        )

        DeleteProfileUseCase().execute(1)

        self.assertFalse(
            Profile.objects.filter(user_id=1).exists()
        )

    def test_should_raise_exception_when_profile_does_not_exist(self):
        with self.assertRaises(Profile.DoesNotExist):
            DeleteProfileUseCase().execute(999)