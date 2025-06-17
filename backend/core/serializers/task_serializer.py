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
        fields = [
            "title",
            "short_description",
            "long_description",
            "due_date",
            "priority",
        ]
        read_only_fields = ["assignee_user", "assignee_team"]
