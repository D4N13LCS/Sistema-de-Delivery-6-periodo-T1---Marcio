from django.db import models

class Profile(models.Model):

    user_id = models.IntegerField(unique=True)

    address = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    balance = models.FloatField(default=200)

    card_registered = models.BooleanField(default=False)

    card_number = models.CharField(
        max_length=16,
        blank=True,
        null=True
    )

    card_name = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    card_expiration = models.CharField(
        max_length=5,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.user_id