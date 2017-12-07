# Third-Party
from rest_framework import serializers

# Local Django
from user.models import User
from core.models import City, Kind
from activity.models import (
        Activity, ActivityLink, ActivityDocument
    )

class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = ('city',)


class KindSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Kind
        fields = ('kind',)


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
    city = CitySerializer();
    kind = KindSerializer()
    image = serializers.ImageField(use_url=False)
    wage_status = serializers.CharField(source="get_wage_status_display")
    starting_date = serializers.DateField(format="%d/%m/%Y")
    activity_links = ActivityLinkSerializer(read_only=True, many=True)
    activity_documents = ActivityDocumentSerializer(read_only=True, many=True)


class ActivitySerializer(ActivityBaseSerializer):

    class Meta:
        model = Activity
        fields = (
            'id', 'city', 'kind', 'address', 'coordinate', 'name', 'starting_date',
            'starting_time', 'end_date', 'end_time', 'wage_status', 'image', 'statement',
            'activity_documents', 'activity_links'
            )


class ActivityListSerializer(ActivityBaseSerializer):

    class Meta:
        model = Activity
        fields = (
            'id', 'city', 'kind', 'name', 'starting_date', 'starting_time', 'wage_status',
            'image'
            )


class UserSerializer(serializers.ModelSerializer):
    city = CitySerializer()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'city')
