from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.http import HttpRequest, HttpResponse
from core.models.task import Task
from core.serializers.task_serializer import TaskSerializer

def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello, world!")

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(assignee_user=user) | Task.objects.filter(assignee_team__members=user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)