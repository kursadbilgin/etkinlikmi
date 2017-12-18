# Local Django
from .base_api_views import ActivityViewSet
from activity.serializers import (
    ActivityLinkSerializerV1, ActivityDocumentSerializerV1, ActivitySerializer,
    ActivityListSerializerV1, ActivityCreateSerializerV1,
    ActivityRetrieveSerializerV1, ActivityUpdateSerializerV1
)


class ActivityViewSetV1(ActivityViewSet):

    def get_serializer_class(self):
        if self.action == 'list':
            return ActivityListSerializerV1
        elif self.action == 'create':
            return ActivityCreateSerializerV1
        elif self.action == 'retrieve':
            return ActivityRetrieveSerializerV1
        elif self.action == 'update':
            return ActivityUpdateSerializerV1
        else:
            return ActivitySerializerV1
