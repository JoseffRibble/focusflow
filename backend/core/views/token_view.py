from rest_framework_simplejwt.views import TokenObtainPairView

from core.serializers import EmailTokenObtainPairSerializer


class TokenLoginView(TokenObtainPairView):
    serializer_class = EmailTokenObtainPairSerializer
