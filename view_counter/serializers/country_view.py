from rest_framework.serializers import ModelSerializer

from view_counter.models import CountryView


class CountryViewS( ModelSerializer ):
    class Meta:
        model = CountryView
        fields = '__all__'