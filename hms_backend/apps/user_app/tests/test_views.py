from django import urls
from django.contrib.auth import get_user_model
import pytest


# @pytest.mark.django_db
# def test_user_register(client, user_data):
#     user_model = get_user_model()
#     assert user_model.objects.count() == 0
#     registration_url = urls.reverse('register')
#     resp = client.post(registration_url, user_data)
#     assert user_model.objects.count() == 1
#     assert resp.status_code == 201


@pytest.mark.django_db
def test_user_login(client, create_test_user, user_data):
    user_model = get_user_model()
    assert user_model.objects.count() == 1
    login_url = urls.reverse('login')
    resp = client.post(login_url, data=user_data)
    assert resp.status_code == 200


@pytest.mark.django_db
def test_user_logout(client, authenticated_user):
    logout_url = urls.reverse('logout')
    resp = client.post(logout_url)
    assert resp.status_code == 200