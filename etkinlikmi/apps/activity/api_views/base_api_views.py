# Third-Party
from rest_framework import viewsets, mixins

# Local Django
from activity.models import Activity, ActivityLink, ActivityDocument
from activity.serializers import (
    ActivityLinkSerializer, ActivityDocumentSerializer, ActivitySerializer,
    ActivityListSerializer, ActivityCreateSerializer,
    ActivityRetrieveSerializer, ActivityUpdateSerializer
)


class ActivityViewSet(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      viewsets.GenericViewSet):
    queryset = Activity.objects.all()

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return ActivityListSerializer
        elif self.action == 'create':
            return ActivityCreateSerializer
        elif self.action == 'retrieve':
            return ActivityRetrieveSerializer
        elif self.action == 'update':
            return ActivityUpdateSerializer
        else:
            return ActivitySerializer

    def perform_create(self, serializer):
        activity = serializer.save(user=self.request.user)
