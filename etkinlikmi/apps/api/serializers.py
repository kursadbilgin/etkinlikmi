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
        fields = ('city', 'coordinate_city')


class CityListSerializer(CitySerializer):

    class Meta:
        model = City
        fields = ('city',)


class KindSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Kind
        fields = ('kind',)


class ActivityAddressSerializer(serializers.ModelSerializer):
    city = CitySerializer()

    class Meta:
        model = ActivityAddress
        fields = ('city', 'address', 'coordinate')


class ActivityAddressListSerializer(ActivityAddressSerializer):
    city = CityListSerializer()

    class Meta:
        model = ActivityAddress
        fields = ('city',)


class ActivityLinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = ActivityLink
        fields =('link',)


class ActivityDocumentSerializer(serializers.ModelSerializer):
    document = serializers.FileField(use_url=False)

    class Meta:
        model = ActivityDocument
        fields = ('document',)


class ActivityBaseSerializer(serializers.ModelSerializer):
    kind = KindSerializer()
    image = serializers.ImageField(use_url=False)
    wage_status = serializers.CharField(source="get_wage_status_display")
    starting_date = serializers.DateField(format="%d/%m/%Y")
    activity_links = ActivityLinkSerializer(read_only=True, many=True)
    activity_documents = ActivityDocumentSerializer(read_only=True, many=True)


class ActivitySerializer(ActivityBaseSerializer):
    activity_addresses = ActivityAddressSerializer(read_only=True, many=True)

    class Meta:
        model = Activity
        fields = (
            'id', 'kind', 'name', 'starting_date', 'starting_time', 'end_date', 'end_time',
            'wage_status', 'image', 'statement', 'activity_documents',
            'activity_links', 'activity_addresses'
            )


class ActivityListSerializer(ActivityBaseSerializer):
    activity_addresses = ActivityAddressListSerializer(read_only=True, many=True)

    class Meta:
        model = Activity
        fields = (
            'id', 'kind', 'name', 'starting_date', 'starting_time', 'wage_status',
            'image', 'activity_addresses'
            )


class UserSerializer(serializers.ModelSerializer):
    city = CityListSerializer()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'city')
