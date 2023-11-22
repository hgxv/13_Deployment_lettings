from .conftest import letting_fixture, client

import pytest
from pytest_django.asserts import assertTemplateUsed


@pytest.mark.django_db
def test_letting(client, letting_fixture):
    response = client.get("/lettings/1/")

    assert response.status_code == 200
    assert "One really good appartment" in response.content.decode()
    assertTemplateUsed(response, "lettings/letting.html")


@pytest.mark.django_db
def test_letting_does_not_exists(client, letting_fixture):
    response = client.get("/lettings/2/")

    assert response.status_code == 404
    assertTemplateUsed(response, "404.html")
