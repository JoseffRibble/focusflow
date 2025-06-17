from rest_framework import permissions, viewsets
from rest_framework.serializers import BaseSerializer

from core.models import Task
from core.serializers.task_serializer import TaskCreateSerializer, TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self) -> type[BaseSerializer]:
        if self.action == "create":
            return TaskCreateSerializer
        return TaskSerializer

    def perform_create(self, serializer: BaseSerializer) -> None:
        print(f"[DEBUG] request.user: {self.request.user} ({type(self.request.user)})")
        serializer.save(assignee_user=self.request.user)
