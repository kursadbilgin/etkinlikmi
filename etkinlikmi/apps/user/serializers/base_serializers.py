# Third-Party
from rest_framework import serializers
from django.utils.translation import ugettext_lazy as _

# Django
from django.conf import settings

# Local Django
from user.models import User
from core.models import City
from core.serializers import CitySerializer, CityListSerializer



class UserSerializer(serializers.ModelSerializer):
    try:
        city = City.objects.get(user_id=id)
        serializer = CitySerializer(many=True, read_only=True)
    except:
        pass

    class Meta:
        model = User
        fields = (
            'id', 'email', 'first_name', 'city', 'last_name', 'is_active',
        )


class UserListSerializer(UserSerializer):

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'city',)


class UserRetrieveSerializer(UserSerializer):
    pass


class UserCreateSerializer(UserSerializer):
    confirm_password = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = (
            'city', 'email', 'first_name', 'last_name', 'password', 'confirm_password'
        )
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate_password(self, value):
        if value != self.initial_data.get('confirm_password', None):
            raise serializers.ValidationError(
                "The two password fields didn't match."
            )

        password_validation.validate_password(value)

        return value


class UserUpdateSerializer(UserSerializer):

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'city')


class UserPasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField()
    new_password = serializers.CharField()
    confirm_new_password = serializers.CharField()

    class Meta:
        fields = ('old_password', 'new_password', 'confirm_new_password')

    def validate_confirm_new_password(self, value):
        if value != self.initial_data['new_password']:
            raise serializers.ValidationError(
                "The two password fields didn't match."
            )

        password_validation.validate_password(value)

        return value

    def validate_old_password(self, value):
        user = self.context['user']

        if not user.check_password(value):
            raise serializers.ValidationError(_(
                'Your old password was entered incorrectly. '
                'Please enter it again.'
            ))

        return value
