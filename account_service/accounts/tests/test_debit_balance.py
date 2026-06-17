from django.test import TestCase

from accounts.application.use_cases.debit_balance import DebitBalanceUseCase
from accounts.models import Profile


class DebitBalanceUseCaseTest(TestCase):

    def test_should_debit_balance(self):
        Profile.objects.create(
            user_id=1,
            balance=200,
        )

        profile = DebitBalanceUseCase().execute(
            user_id=1,
            value=80,
        )

        self.assertEqual(profile.balance, 120)

    def test_should_raise_exception_when_balance_is_insufficient(self):
        Profile.objects.create(
            user_id=2,
            balance=30,
        )

        with self.assertRaises(ValueError):
            DebitBalanceUseCase().execute(
                user_id=2,
                value=100,
            )