# Standart Library
import datetime

# Third-Party
from rest_framework import serializers

# Django
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

# Local Django
from user.models import User
from core.models import City, Kind
from core.serializers import CitySerializer, KindSerializer
from activity.models import Activity, ActivityLink, ActivityDocument


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
    city = CitySerializer()
    kind = KindSerializer()
    wage_status = serializers.CharField(source="get_wage_status_display")
    starting_date = serializers.DateField(format="%d/%m/%Y")
    starting_time = serializers.TimeField(format="%H:%M")
    activity_links = ActivityLinkSerializer(read_only=True, many=True)
    activity_documents = ActivityDocumentSerializer(read_only=True, many=True)

    class Meta:
        model = Activity
        fields = (
            'id', 'city', 'kind', 'address', 'coordinate', 'name', 'starting_date',
            'starting_time', 'end_date', 'end_time', 'wage_status', 'image',
            'statement', 'activity_documents', 'activity_links'
        )

    def get_image(self, obj):
        if obj.image:
            return settings.DOMAIN + obj.image.url
        else:
            return None


class ActivityListSerializer(ActivitySerializer):

    class Meta:
        model = Activity
        fields = (
            'id', 'city', 'kind', 'name', 'starting_date', 'starting_time', 'wage_status',
            'image'
        )


class ActivityCreateSerializer(serializers.ModelSerializer):
    wage_status = serializers.CharField()

    class Meta:
        model = Activity
        fields = (
            'id', 'city', 'kind', 'name', 'address', 'coordinate', 'starting_date',
            'starting_time', 'end_date', 'end_time', 'wage_status', 'image', 'statement'
        )


class ActivityRetrieveSerializer(ActivitySerializer):
    pass


class ActivityUpdateSerializer(ActivitySerializer):

    class Meta:
        model = Activity
        fields = (
            'id', 'city', 'kind', 'address', 'coordinate', 'name', 'starting_date',
            'starting_time', 'end_date', 'end_time', 'wage_status', 'image',
            'statement', 'activity_documents', 'activity_links'
        )
