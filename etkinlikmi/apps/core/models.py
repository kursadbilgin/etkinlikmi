# Third-Party
from geoposition.fields import GeopositionField

# Django
from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _


class DateModel(models.Model):
    create_date = models.DateTimeField(
        verbose_name=_('Create Date'), auto_now_add=True, editable=False
    )
    update_date = models.DateTimeField(
        verbose_name=_('Update Date'), auto_now=True, editable=False
    )

    class Meta:
        abstract = True


class City(models.Model):
    city = models.CharField(verbose_name=_('City'), max_length=55, unique=True)
    coordinate_city = GeopositionField(verbose_name=_('Coordinate'), null=True)

    class Meta:
        verbose_name=_(u'City')
        verbose_name_plural=_(u'Cities')

    def __str__(self):
        return self.city


class Kind(models.Model):
    kind = models.CharField(verbose_name=_('Kind'), max_length=50, unique=True)

    class Meta:
        verbose_name=_(u'Kind')
        verbose_name_plural=_(u'Kinds')

    def __str__(self):
        return self.kind


class SocialAccount(DateModel):
    name = models.CharField(
        verbose_name=_('Social Account'), max_length=50, unique=True
    )
    style_class = models.CharField(
        verbose_name=_('Style Class'), max_length=50, null=True, blank=True
    )

    class Meta:
        verbose_name=_(u'Social Account')
        verbose_name_plural=_(u'Social Accounts')

    def __str__(self):
        return self.name
