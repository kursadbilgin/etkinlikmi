# Third-Party
from rest_framework import viewsets, mixins
from djoser.views import LoginView as _LoginView

# Local Django
from user.models import User
from core.models import City, Kind, SocialAccount
from core.serializers import (
    CitySerializer, KindSerializer, SocialAccountSerializer
)


class LoginView(_LoginView):

    def _action(self, serializer):
        action = super(LoginView, self)._action(serializer)

        action.data.update({
            'user_id': serializer.user.id,
        })

        return action


class CityViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

    def get_permissions(self):
        permissions = super(CityViewSet, self).get_permissions()

        if self.action in ['list']:
            return []

        return permissions


class KindViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Kind.objects.all()
    serializer_class = KindSerializer

    def get_permissions(self):
        permissions = super(KindViewSet, self).get_permissions()

        if self.action in ['list']:
            return []

        return permissions


class SocialAccountViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = SocialAccount.objects.all()
    serializer_class = SocialAccountSerializer
