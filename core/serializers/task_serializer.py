from typing import Any

from rest_framework import serializers

from core.models.task import Task
from core.serializers.team_serializer import TeamSerializer
from core.serializers.user_serializer import UserSerializer


class TaskSerializer(serializers.ModelSerializer):
    assignee_user = UserSerializer(read_only=True)
    assignee_team = TeamSerializer(read_only=True)

    class Meta:
        model = Task
        fields = "__all__"


class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"

    def create(self, validated_data: dict[str, Any]) -> Task:
        return Task.objects.create_task(**validated_data)
