# Local Django
from .base_serializers import (
    CitySerializer, CityListSerializer,
    KindSerializer, KindListSerializer, SocialAccountSerializer
)


class CitySerializerV1(CitySerializer):
    pass


class CityListSerializerV1(CityListSerializer):
    pass


class KindSerializerV1(KindSerializer):
    pass


class KindListSerializerV1(KindListSerializer):
    pass


class SocialAccountSerializerV1(SocialAccountSerializer):
    pass
