# Third-Party
from rest_framework import serializers

# Local Django
from user.models import User
from core.models import City, Kind
from activity.models import (
        Activity, ActivityAddress, ActivityLink, ActivityDocument
    )

class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = ('city',)


class KindSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Kind
        fields = ('name',)


class ActivityAddressSerializer(serializers.ModelSerializer):
    city = serializers.CharField()

    class Meta:
        model = ActivityAddress
        fields = ('city', 'address')

class ActivityLinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = ActivityLink
        fields =('link',)

class ActivityDocumentSerializer(serializers.ModelSerializer):
    document = serializers.FileField(use_url=False)

    class Meta:
        model = ActivityDocument
        fields = ('document',)


class ActivitySerializer(serializers.ModelSerializer):
    cities = CitySerializer(read_only=True, many=True)
    image = serializers.ImageField(use_url=False)
    activity_addresses = ActivityAddressSerializer(read_only=True, many=True)
    activity_links = ActivityLinkSerializer(read_only=True, many=True)
    activity_documents = ActivityDocumentSerializer(read_only=True, many=True)

    class Meta:
        model = Activity
        fields = (
            'name', 'starting_date', 'starting_time', 'end_date', 'end_time',
            'wage_status', 'cities','image', 'statement', 'activity_documents',
            'activity_links','activity_addresses'
            )


class UserSerializer(serializers.ModelSerializer):
    city = serializers.CharField()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'city')
