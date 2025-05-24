from rest_framework import serializers
from core.models.task import Task
from core.models.user import User
from core.models.team import Team

from core.serializers.team_serializer import TeamSerializer
from core.serializers.user_serializer import UserSerializer


class TaskSerializer(serializers.ModelSerializer):
    assignee_user = UserSerializer(read_only=True)
    assignee_team = TeamSerializer(read_only=True)

    class Meta:
        model = Task
        fields = "__all__"
