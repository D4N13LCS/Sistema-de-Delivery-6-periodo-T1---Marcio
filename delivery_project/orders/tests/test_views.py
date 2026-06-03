import pytest

from django.contrib.auth.models import User


@pytest.mark.django_db
def test_historico_logado(client):

    user = User.objects.create_user(
        username="teste",
        password="123456"
    )

    client.login(
        username="teste",
        password="123456"
    )

    response = client.get(
        "/historico/"
    )

    assert response.status_code == 200