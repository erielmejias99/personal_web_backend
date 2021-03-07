from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, \
    DestroyModelMixin
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from file.models import Image
from file.serializers import ImageS
from permission import IsSuperUser


class ImageViewSet( ListModelMixin, RetrieveModelMixin,
                     CreateModelMixin, UpdateModelMixin,
                     DestroyModelMixin, GenericViewSet ):

    queryset = Image.objects.all()
    serializer_class = ImageS
    filter_backends = [ DjangoFilterBackend, ]
    filterset_fields = [ 'place' ]

    def get_permissions(self):

        if self.action == 'list' or self.action == 'retrieve':
            return AllowAny(),
        else:
            return IsAuthenticated(), IsSuperUser()