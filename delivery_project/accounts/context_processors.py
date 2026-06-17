from accounts.gateways.account_gateway import AccountGateway


def profile_context(request):
    if request.user.is_authenticated:
        profile = AccountGateway.get_profile(request.user.id)

        if profile is None:
            profile = {}

        return {
            "profile": profile
        }

    return {
        "profile": {}
    }