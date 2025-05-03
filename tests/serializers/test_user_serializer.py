import pytest

from core.serializers.user_serializer import UserRegistrationSerializer


@pytest.mark.django_db
def test_user_registration_serializer_valid():
    data = {"username": "tester", "email": "test@example.com", "password": "secure123"}
    serializer = UserRegistrationSerializer(data=data)
    assert serializer.is_valid(), serializer.errors
    user = serializer.save()
    assert user.email == "test@example.com"
