from .conftest import client, letting_fixture

import pytest
from pytest_django.asserts import assertTemplateUsed


@pytest.mark.django_db
def test_index(client, letting_fixture):
    response = client.get("/lettings/")

    assert response.status_code == 200
    assert "One really good appartment" in response.content.decode()
    assertTemplateUsed(response, "lettings/index.html")
