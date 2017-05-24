# Third-Party
from rest_framework import viewsets

# Local Django
from user.models import User
from activity.models import Activity

# Api
from api.serializers import UserSerializer, ActivityListSerializer, ActivitySerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ActivityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Activity.objects.all()
    def get_serializer_class(self):
        if self.action == 'list':
            return ActivityListSerializer
        else:
            return ActivitySerializer


LIST = (
     (r'user', UserViewSet),
     (r'activity', ActivityViewSet),
 )
