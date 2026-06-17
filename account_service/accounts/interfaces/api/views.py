import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from accounts.application.use_cases.create_profile import CreateProfileUseCase
from accounts.application.use_cases.get_profile import GetProfileUseCase
from accounts.application.use_cases.update_profile import UpdateProfileUseCase
from accounts.application.use_cases.credit_balance import CreditBalanceUseCase
from accounts.application.use_cases.debit_balance import DebitBalanceUseCase
from accounts.application.use_cases.delete_profile import DeleteProfileUseCase


@csrf_exempt
def create_profile(request):

    if request.method != "POST":
        return JsonResponse(
            {"error": "Method not allowed"},
            status=405,
        )

    data = json.loads(request.body)

    profile, _ = CreateProfileUseCase().execute(
        user_id=data["user_id"],
        balance=data.get("balance", 200),
        address=data.get("address", ""),
    )

    return JsonResponse(
        {
            "user_id": profile.user_id,
            "balance": profile.balance,
            "address": profile.address,
        },
        status=201,
    )


def get_profile(request, user_id):

    if request.method != "GET":
        return JsonResponse(
            {"error": "Method not allowed"},
            status=405,
        )

    try:

        profile = GetProfileUseCase().execute(user_id)

        return JsonResponse(
            {
                "user_id": profile.user_id,
                "balance": profile.balance,
                "address": profile.address,
                "card_registered": profile.card_registered,
                "card_number": profile.card_number,
                "card_name": profile.card_name,
                "card_expiration": profile.card_expiration,
            }
        )

    except Exception:

        return JsonResponse(
            {"error": "Profile not found"},
            status=404,
        )


@csrf_exempt
def update_profile(request, user_id):

    if request.method != "PUT":
        return JsonResponse(
            {"error": "Method not allowed"},
            status=405,
        )

    try:

        data = json.loads(request.body)

        profile = UpdateProfileUseCase().execute(
            user_id=user_id,
            address=data.get("address"),
            card_number=data.get("card_number"),
            card_name=data.get("card_name"),
            card_expiration=data.get("card_expiration"),
        )

        return JsonResponse(
            {
                "message": "Profile updated successfully",
                "user_id": profile.user_id,
                "address": profile.address,
            }
        )

    except Exception:

        return JsonResponse(
            {"error": "Profile not found"},
            status=404,
        )


@csrf_exempt
def delete_profile(request, user_id):

    if request.method != "DELETE":
        return JsonResponse(
            {"error": "Method not allowed"},
            status=405,
        )

    try:

        DeleteProfileUseCase().execute(user_id)

        return JsonResponse(
            {
                "message": "Profile deleted successfully",
            }
        )

    except Exception:

        return JsonResponse(
            {
                "error": "Profile not found",
            },
            status=404,
        )


@csrf_exempt
def credit_balance(request):

    if request.method != "POST":
        return JsonResponse(
            {"error": "Method not allowed"},
            status=405,
        )

    data = json.loads(request.body)

    profile = CreditBalanceUseCase().execute(
        user_id=data["user_id"],
        value=data["value"],
    )

    return JsonResponse(
        {
            "status": "success",
            "balance": profile.balance,
        }
    )


@csrf_exempt
def debit_balance(request):

    if request.method != "POST":
        return JsonResponse(
            {"error": "Method not allowed"},
            status=405,
        )

    data = json.loads(request.body)

    try:

        profile = DebitBalanceUseCase().execute(
            user_id=data["user_id"],
            value=data["value"],
        )

        return JsonResponse(
            {
                "status": "success",
                "balance": profile.balance,
            }
        )

    except ValueError as exc:

        return JsonResponse(
            {"error": str(exc)},
            status=400,
        )