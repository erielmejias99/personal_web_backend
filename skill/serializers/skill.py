from rest_framework.serializers import ModelSerializer

from skill.models import Skill


class SkillS( ModelSerializer ):
    class Meta:
        model = Skill
        fields = '__all__'