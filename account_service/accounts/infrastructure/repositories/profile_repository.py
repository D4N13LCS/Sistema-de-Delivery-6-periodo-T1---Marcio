from accounts.models import Profile

class ProfileRepository:

    @staticmethod
    def get_by_user_id(user_id):
        return Profile.objects.get(user_id=user_id)

    @staticmethod
    def get_or_create(user_id, **defaults):
        return Profile.objects.get_or_create(
            user_id=user_id,
            defaults=defaults,
        )

    @staticmethod
    def save(profile):
        profile.save()
        return profile

    @staticmethod
    def delete(profile):
        profile.delete()