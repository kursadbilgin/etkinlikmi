# Local Django
from .base_serializers import (
    UserSerializer, UserListSerializer, UserCreateSerializer,
    UserRetrieveSerializer, UserUpdateSerializer,
    UserPasswordChangeSerializer
)
from core.serializers import CitySerializerV1, CityListSerializerV1


class UserSerializerV1(UserSerializer):
    city = CitySerializerV1(many=True, read_only=True)


class UserListSerializerV1(UserListSerializer):
    pass


class UserRetrieveSerializerV1(UserRetrieveSerializer):
    pass


class UserCreateSerializerV1(UserCreateSerializer):
    city = CityListSerializerV1(many=True, read_only=True)


class UserUpdateSerializerV1(UserUpdateSerializer):
    city = CityListSerializerV1(many=True, read_only=True)


class UserPasswordChangeSerializerV1(UserPasswordChangeSerializer):
    pass
