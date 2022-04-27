import pytest
from django.contrib.auth import get_user_model


@pytest.fixture
def user_data():
    return {
        # "email": "testmail@mail.ru",
        "username": "123456789000",
        "first_name": "Daulet",
        "last_name": "Abduali",
        "password": "poiuy123!"
    }


@pytest.fixture
def create_test_user(user_data):
    user_model = get_user_model()
    test_user = user_model.objects.create_user(**user_data)
    test_user.set_password(user_data.get('password'))
    return test_user


@pytest.fixture
def authenticated_user(client, user_data):
    user_model = get_user_model()
    test_user = user_model.objects.create_user(**user_data)
    test_user.set_password(user_data.get('password'))
    test_user.save()
    client.login(**user_data)
    return test_user