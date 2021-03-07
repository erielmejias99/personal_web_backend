from rest_framework.serializers import ModelSerializer

from experience.models import Experience


class ExperienceS( ModelSerializer ):
    class Meta:
        model = Experience
        fields = '__all__'
