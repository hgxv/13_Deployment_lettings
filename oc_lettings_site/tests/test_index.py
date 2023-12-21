from pytest_django.asserts import assertTemplateUsed


def test_index(client):
    response = client.get("/")

    assert response.status_code == 200
    assertTemplateUsed(response, "index.html")
