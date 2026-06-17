from behave import given, when, then
from django.test import Client

from accounts.models import Profile


@given("a user id 1")
def step_given_user_id(context):

    Profile.objects.filter(user_id=1).delete()

    context.client = Client()
    context.user_id = 1


@given("an existing profile for user 1")
def step_existing_profile(context):
    context.client = Client()

    Profile.objects.update_or_create(
        user_id=1,
        defaults={
            "balance": 100,
            "address": "Old Address",
        },
    )

    context.user_id = 1


@when('a profile is created with balance 200 and address "Main Street"')
def step_create_profile(context):
    context.response = context.client.post(
        "/api/accounts/profile/create/",
        data={
            "user_id": context.user_id,
            "balance": 200,
            "address": "Main Street",
        },
        content_type="application/json",
    )


@when("I request the profile")
def step_get_profile(context):
    context.response = context.client.get(
        f"/api/accounts/profile/{context.user_id}/"
    )


@when('I update the profile address to "New Address"')
def step_update_profile(context):
    context.response = context.client.put(
        f"/api/accounts/profile/{context.user_id}/update/",
        data={
            "address": "New Address",
        },
        content_type="application/json",
    )


@when("I delete the profile")
def step_delete_profile(context):
    context.response = context.client.delete(
        f"/api/accounts/profile/{context.user_id}/delete/"
    )


@then("the response status should be 201")
def step_status_201(context):
    assert context.response.status_code == 201


@then("the response status should be 200")
def step_status_200(context):
    assert context.response.status_code == 200


@then("the returned user id should be 1")
def step_returned_user(context):
    assert context.response.json()["user_id"] == 1


@then("the profile balance should be 200")
def step_profile_balance(context):
    print(context.response.json())
    assert float(context.response.json()["balance"]) == 200.0


@then('the profile address should be "New Address"')
def step_profile_address(context):
    profile = Profile.objects.get(user_id=1)
    assert profile.address == "New Address"