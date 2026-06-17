from behave import given, when, then
from django.test import Client

from accounts.models import Profile


@given("a profile with balance 100")
def step_balance_100(context):
    context.client = Client()

    Profile.objects.update_or_create(
        user_id=1,
        defaults={
            "balance": 100,
            "address": "",
        },
    )


@given("a profile with balance 20")
def step_balance_20(context):
    context.client = Client()

    Profile.objects.update_or_create(
        user_id=1,
        defaults={
            "balance": 20,
            "address": "",
        },
    )


@when("I credit 50")
def step_credit(context):
    context.response = context.client.post(
        "/api/accounts/balance/credit/",
        data={
            "user_id": 1,
            "value": 50,
        },
        content_type="application/json",
    )


@when("I debit 40")
def step_debit_40(context):
    context.response = context.client.post(
        "/api/accounts/balance/debit/",
        data={
            "user_id": 1,
            "value": 40,
        },
        content_type="application/json",
    )


@when("I debit 50")
def step_debit_50(context):
    context.response = context.client.post(
        "/api/accounts/balance/debit/",
        data={
            "user_id": 1,
            "value": 50,
        },
        content_type="application/json",
    )


@then("the balance should become 150")
def step_balance_150(context):
    profile = Profile.objects.get(user_id=1)
    assert profile.balance == 150


@then("the balance should become 60")
def step_balance_60(context):
    profile = Profile.objects.get(user_id=1)
    assert profile.balance == 60


@then("the response status should be 400")
def step_status_400(context):
    assert context.response.status_code == 400