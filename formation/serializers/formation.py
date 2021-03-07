from rest_framework.serializers import ModelSerializer

from formation.models import Formation


class FormationS( ModelSerializer ):
    class Meta:
        model = Formation
        fields = '__all__'
