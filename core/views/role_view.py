from typing import Any

from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import User


class RoleUpdateView(APIView):
    def post(
        self, request: Request, user_id: int, *args: Any, **kwargs: Any
    ) -> Response:
        role: str = request.data.get("role", "")
        user = User.objects.filter(id=user_id).first()
        if not user:
            return Response(
                {"error": "User not found"}, status=status.HTTP_404_NOT_FOUND
            )
        user.role = role
        user.save()
        return Response({"id": user.id, "role": user.role}, status=status.HTTP_200_OK)
