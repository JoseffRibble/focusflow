from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.http import HttpRequest, HttpResponse
from core.models.task import Task
from core.serializers.task_serializer import TaskSerializer


def index(request):
    return HttpResponse("Hello, world")
