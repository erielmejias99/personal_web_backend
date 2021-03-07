from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, \
    DestroyModelMixin
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from formation.models import Formation
from formation.serializers import FormationS
from permission import IsSuperUser


class FormationViewSet( ListModelMixin, RetrieveModelMixin,
                     CreateModelMixin, UpdateModelMixin,
                     DestroyModelMixin, GenericViewSet ):

    queryset = Formation.objects.all()
    serializer_class = FormationS

    def get_permissions(self):

        if self.action == 'list' or self.action == 'retrieve':
            return AllowAny(),
        else:
            return IsAuthenticated(), IsSuperUser()