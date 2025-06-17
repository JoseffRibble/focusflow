from core.serializers.auth_serializer import LoginSerializer


def test_login_serializer_valid():
    data = {"email": "u@e.com", "password": "secure123"}
    serializer = LoginSerializer(data=data)
    assert serializer.is_valid()
