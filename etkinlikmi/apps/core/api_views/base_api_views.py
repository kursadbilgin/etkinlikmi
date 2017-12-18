# Third-Party
from rest_framework import viewsets, mixins

# Local Django
from user.models import User
from core.models import City, Kind, SocialAccount
from core.serializers import (
    CitySerializer, KindSerializer, SocialAccountSerializer
)


class CityViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class KindViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Kind.objects.all()
    serializer_class = KindSerializer


class SocialAccountViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = SocialAccount.objects.all()
    serializer_class = SocialAccountSerializer
