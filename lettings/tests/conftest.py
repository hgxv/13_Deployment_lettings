from django.test import Client
from ..models import Letting, Address

import pytest

client = Client()


@pytest.fixture
def letting_fixture():
    address_obj = Address.objects.create(
        number=13310,
        street="Warwick Blvd",
        city="Newport News",
        state="VT",
        zip_code=23602,
        country_iso_code="USA",
    )

    letting = Letting.objects.create(
        title="One really good appartment", address=address_obj
    )
    return letting
