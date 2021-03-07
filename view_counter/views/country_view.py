from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from permission import IsSuperUser
from view_counter.models import CountryView
from view_counter.serializers import CountryViewS


class CountryViewSet( ListModelMixin, RetrieveModelMixin, GenericViewSet ):

    queryset = CountryView.objects.all()
    serializer_class = CountryViewS

    def get_permissions(self):
        return IsAuthenticated(), IsSuperUser()