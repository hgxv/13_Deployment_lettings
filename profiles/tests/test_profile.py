import pytest
from pytest_django.asserts import assertTemplateUsed


@pytest.mark.django_db
def test_profile(client, profile_fixture):
    response = client.get("/profiles/PC_crowdsurfer88/")

    assert response.status_code == 200
    assert b"PC_crowdsurfer88" in response.content
    assert b"Peter" in response.content
    assertTemplateUsed(response, "profiles/profile.html")


@pytest.mark.django_db
def test_profile_doesnt_exists(client, profile_fixture):
    response = client.get("/profiles/PatrickNotHere/")

    assert response.status_code == 404
    assertTemplateUsed(response, "404.html")
