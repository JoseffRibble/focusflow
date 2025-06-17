from core.models import Team
from core.serializers.team_serializer import TeamSerializer


def test_team_serializer_fields():
    team = Team(name="QA", description="Quality Assurance")
    serializer = TeamSerializer(team)
    assert set(serializer.data.keys()) == {"id", "name", "description"}
