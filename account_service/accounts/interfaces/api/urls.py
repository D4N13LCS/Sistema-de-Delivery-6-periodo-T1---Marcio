from django.urls import path

from .views import (
    create_profile,
    get_profile,
    update_profile,
    delete_profile,
    debit_balance,
    credit_balance,
)

urlpatterns = [

    # Perfil
    path(
        "profile/create/",
        create_profile,
        name="create_profile",
    ),

    path(
        "profile/<int:usuario_id>/",
        get_profile,
        name="get_profile",
    ),

    path(
        "profile/<int:usuario_id>/update/",
        update_profile,
        name="update_profile",
    ),

    path(
        "profile/<int:usuario_id>/delete/",
        delete_profile,
        name="delete_profile",
    ),

    # Saldo
    path(
        "balance/debit/",
        debit_balance,
        name="debit_balance",
    ),

    path(
        "balance/credit/",
        credit_balance,
        name="credit_balance",
    ),
]