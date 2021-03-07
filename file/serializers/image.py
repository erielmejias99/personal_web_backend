from rest_framework.serializers import ModelSerializer

from file.models import Image


class ImageS( ModelSerializer ):
    class Meta:
        model = Image
        fields = '__all__'
