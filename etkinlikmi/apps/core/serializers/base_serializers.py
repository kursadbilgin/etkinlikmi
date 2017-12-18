# Third-Party
from rest_framework import serializers

# Django
from django.utils.translation import ugettext_lazy as _

# Local Django
from core.models import City, Kind, SocialAccount


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = ('id', 'city',)


class CityListSerializer(CitySerializer):

    class Meta:
        model = City
        fields = ('city',)


class KindSerializer(serializers.ModelSerializer):

    class Meta:
        model = Kind
        fields = ('id', 'kind',)


class KindListSerializer(KindSerializer):

    class Meta:
        model = Kind
        fields = ('kind',)


class SocialAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = SocialAccount
        fields = ('style_class',)
