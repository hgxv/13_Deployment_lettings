from .conftest import client

import pytest


@pytest.mark.django_db
def test_page_doesnt_exist(client):
    response = client.get("/fffff/")

    assert response.status_code == 404
