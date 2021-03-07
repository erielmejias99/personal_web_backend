from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, \
    DestroyModelMixin
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from permission import IsSuperUser
from personal_data.models import PersonalData
from personal_data.serializers import PersonalDataS


class PersonalDataViewSet( ListModelMixin, RetrieveModelMixin,
                     CreateModelMixin, UpdateModelMixin,
                     DestroyModelMixin, GenericViewSet ):

    queryset = PersonalData.objects.all()
    serializer_class = PersonalDataS

    def get_permissions(self):

        if self.action == 'list' or self.action == 'retrieve':
            return AllowAny(),
        else:
            return IsAuthenticated(), IsSuperUser()