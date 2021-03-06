
from rest_framework.serializers import ModelSerializer

from status.models import Status


class StatusS( ModelSerializer ):
    class Meta:
        model = Status
        fields = '__all__'