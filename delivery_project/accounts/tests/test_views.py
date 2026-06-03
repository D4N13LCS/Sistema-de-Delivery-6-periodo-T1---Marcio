import pytest

from django.urls import reverse


@pytest.mark.django_db
def test_register_page(client):

    response = client.get(
        reverse("register")
    )

    assert response.status_code == 200