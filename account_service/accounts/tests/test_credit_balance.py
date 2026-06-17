from django.test import TestCase

from accounts.application.use_cases.credit_balance import CreditBalanceUseCase
from accounts.models import Profile


class CreditBalanceUseCaseTest(TestCase):

    def test_should_credit_balance(self):
        Profile.objects.create(
            user_id=1,
            balance=100,
        )

        profile = CreditBalanceUseCase().execute(
            user_id=1,
            value=50,
        )

        self.assertEqual(profile.balance, 150)
    
    def test_should_credit_zero(self):
        Profile.objects.create(
            user_id=2,
            balance=100,
        )

        profile = CreditBalanceUseCase().execute(
            user_id=2,
            value=0,
        )

        self.assertEqual(profile.balance, 100)