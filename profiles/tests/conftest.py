from django.test import Client
from django.contrib.auth.models import User
from ..models import Profile

import pytest

client = Client()


@pytest.fixture
def profile_fixture():
    user_obj = User.objects.create(
        first_name="Peter",
        last_name="Crawley",
        email="peter.crawley@gmail.com",
        username="PC_crowdsurfer88",
    )
    user_obj.set_password("password")

    profile = Profile.objects.create(user=user_obj, favorite_city="Salt Lake City")

    return profile
