from typing import Any

from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)


class EmailTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = "email"  # Optional, for compatibility

    def validate(self, attrs: dict[str, Any]) -> dict[str, Any]:
        email = attrs.get("email")
        password = attrs.get("password")

        if not email or not password:
            raise AuthenticationFailed("Email and password are required")

        # Use 'username' here for compatibility with default backend
        user = authenticate(
            request=self.context.get("request"), username=email, password=password
        )

        if not user:
            raise AuthenticationFailed("Invalid credentials")

        self.user = user
        return super().validate(attrs)


class TokenLoginView(TokenObtainPairView):
    serializer_class = EmailTokenObtainPairSerializer
