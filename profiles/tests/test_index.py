import pytest
from pytest_django.asserts import assertTemplateUsed


@pytest.mark.django_db
def test_index(client, profile_fixture):
    response = client.get("/profiles/")

    assert response.status_code == 200
    assert "PC_crowdsurfer88" in response.content.decode()
    assertTemplateUsed(response, "profiles/index.html")
