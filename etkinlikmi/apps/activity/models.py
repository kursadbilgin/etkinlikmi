# Standart Library
import os

# Third-Party
from geoposition.fields import GeopositionField

# Django
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Local Django
from user.models import User
from core.models import DateModel, Kind, City, SocialAccount


BOOL_CHOICES = ('0', _('Wage Earner')), ('1', _('Free'))


def set_activity_image_upload_path(instance, filename):
    return os.path.join("activity_%d" % instance.id, 'images', filename)


class Activity(DateModel):
    user = models.ForeignKey(verbose_name=_('User'), to=User)

    # Base
    city = models.ForeignKey(verbose_name=_('City'), to=City, related_name="activity_city")
    kind = models.ForeignKey(verbose_name=_('Kind'), to=Kind)
    address = models.TextField(verbose_name=_('Address'), null=True, blank=True)
    coordinate = GeopositionField(verbose_name=_('Coordinate'), null=True, blank=True)
    name = models.CharField(verbose_name=_('Name'), max_length=50)

    # Time
    starting_date = models.DateField(verbose_name=_('Starting Date'))
    end_date = models.DateField(verbose_name=_('End Date'), null=True, blank=True)
    starting_time = models.TimeField(verbose_name=_('Starting Time'))
    end_time = models.TimeField(verbose_name=_('End Time'), null=True, blank=True)

    # Wage Status
    wage_status = models.CharField(
        max_length=10 ,verbose_name=_('Wage Status'), choices=BOOL_CHOICES
    )

    # Image
    image = models.ImageField(
        verbose_name=_('Image'), null=True, blank=True,
        upload_to=set_activity_image_upload_path
    )

    # Statement
    statement = models.TextField(verbose_name=_('Statement'), max_length=1000)

    class Meta:
        verbose_name=_(u'Activity')
        verbose_name_plural=_(u'Activitys')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.pk is None:
            saved_image = self.image
            self.image = None
            super(Activity, self).save(*args, **kwargs)
            self.image = saved_image
        else:
            return super(Activity, self).save(*args, **kwargs)


class ActivityLink(DateModel):
    activity = models.ForeignKey(
        verbose_name=_('Activity'), to=Activity, related_name='activity_links'
    )
    social_account = models.ForeignKey(
        verbose_name=_('Social Account'), to=SocialAccount
    )
    link = models.URLField(verbose_name=_('Link'), null=True)

    class Meta:
        verbose_name=_('Activity Link')
        verbose_name_plural=_('Activity Links')


def set_activity_document_upload_path(instance, filename):
    return os.path.join("activity_%d" % instance.activity.id, 'document', filename)


class ActivityDocument(DateModel):
    activity = models.ForeignKey(
        verbose_name=_('Activity'), to=Activity, related_name='activity_documents'
    )
    document = models.FileField(
        verbose_name=_('Document'), upload_to=set_activity_document_upload_path
    )

    class Meta:
        verbose_name=_('Activity Document')
        verbose_name_plural=_('Activity Documents')

    def get_size(self):
        return self.document._get_size()

    get_size.short_description =  _('Size')
