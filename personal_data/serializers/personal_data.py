from rest_framework.serializers import ModelSerializer

from personal_data.models import PersonalData


class PersonalDataS( ModelSerializer ):
    class Meta:
        model = PersonalData
        fields = '__all__'
