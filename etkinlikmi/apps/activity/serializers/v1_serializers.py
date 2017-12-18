# Local Django
from .base_serializers import (
    ActivityLinkSerializer, ActivityDocumentSerializer,
    ActivitySerializer, ActivityListSerializer,
    ActivityCreateSerializer, ActivityRetrieveSerializer,
    ActivityUpdateSerializer
)
from core.serializers import CitySerializerV1, KindSerializerV1


class ActivityLinkSerializerV1(ActivityLinkSerializer):
    pass


class ActivityDocumentSerializerV1(ActivityDocumentSerializer):
    pass


class ActivityListSerializerV1(ActivityListSerializer):
    pass


class ActivityCreateSerializerV1(ActivityCreateSerializer):
    city = CitySerializerV1(read_only=True, many=True)
    kind = KindSerializerV1(read_only=True, many=True)


class ActivityRetrieveSerializerV1(ActivityRetrieveSerializer):
    pass


class ActivityUpdateSerializerV1(ActivityUpdateSerializer):
    city = CitySerializerV1(read_only=True, many=True)
    kind = KindSerializerV1(read_only=True, many=True)
