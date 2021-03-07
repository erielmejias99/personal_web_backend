from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, \
    DestroyModelMixin
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from experience.models import Experience
from experience.serializers import ExperienceS
from permission import IsSuperUser


class ExperienceViewSet( ListModelMixin, RetrieveModelMixin,
                     CreateModelMixin, UpdateModelMixin,
                     DestroyModelMixin, GenericViewSet ):

    queryset = Experience.objects.all()
    serializer_class = ExperienceS

    def get_permissions(self):

        if self.action == 'list' or self.action == 'retrieve':
            return AllowAny(),
        else:
            return IsAuthenticated(), IsSuperUser()