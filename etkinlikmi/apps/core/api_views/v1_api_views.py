# Local Django
from .base_api_views import CityViewSet, KindViewSet, SocialAccountViewSet
from core.serializers import (
    CitySerializer, CitySerializerV1, KindSerializer, SocialAccountSerializer
)
from core.models import City, Kind ,SocialAccount


class CityViewSetV1(CityViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class KindViewSetV1(KindViewSet):
    queryset = Kind.objects.all()
    serializer_class = KindSerializer


class SocialAccountViewSetV1(SocialAccountViewSet):
    queryset = SocialAccount.objects.all()
    serializer_class = SocialAccountSerializer
