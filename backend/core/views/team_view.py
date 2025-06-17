from rest_framework import viewsets

from core.models import Team
from core.serializers.team_serializer import TeamSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
