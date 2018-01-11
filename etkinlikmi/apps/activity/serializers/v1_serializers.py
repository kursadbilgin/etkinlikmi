# Local Django
from .base_serializers import (
    ActivityLinkSerializer, ActivityDocumentSerializer,
    ActivitySerializer, ActivityListSerializer,
    ActivityCreateSerializer, ActivityRetrieveSerializer,
    ActivityUpdateSerializer
)


class ActivityLinkSerializerV1(ActivityLinkSerializer):
    pass


class ActivityDocumentSerializerV1(ActivityDocumentSerializer):
    pass


class ActivityListSerializerV1(ActivityListSerializer):
    pass


class ActivityCreateSerializerV1(ActivityCreateSerializer):
    pass


class ActivityRetrieveSerializerV1(ActivityRetrieveSerializer):
    pass


class ActivityUpdateSerializerV1(ActivityUpdateSerializer):
    pass
