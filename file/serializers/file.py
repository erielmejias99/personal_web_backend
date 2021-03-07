from rest_framework.serializers import ModelSerializer

from file.models import File


class FileS( ModelSerializer ):
    class Meta:
        model = File
        fields = '__all__'
