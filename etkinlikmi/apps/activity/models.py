# Standart Library
import os

# Third-Party
from geoposition.fields import GeopositionField

# Django
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Local Django
from user.models import User
from core.models import DateModel, Kind, City

def set_activity_image_upload_path(instance, filename):
    return os.path.join("activity_%d" % instance.id, 'images', filename)


class Activity(DateModel):
    user = models.ForeignKey(verbose_name=_('User'), to=User)
    kind = models.ForeignKey(verbose_name=_('Kind'), to=Kind)
    name = models.CharField(verbose_name=_('Name'), max_length=50)
    date = models.DateField(verbose_name=_('Date'))
    image = models.ImageField(
        verbose_name=_('Image'), null=True, blank=True,
        upload_to=set_activity_image_upload_path
    )
    city = models.ForeignKey(verbose_name=_('City'), to=City)
    address = models.TextField(verbose_name=_('Address'), null=True, blank=True)
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

        return super(Activity, self).save(*args, **kwargs)


class ActivityMap(DateModel):
    coordinates = GeopositionField(verbose_name=_('Coordinates'))
    activity = models.ForeignKey(
        verbose_name=_('Activity'), to='activity.Activity'
    )

    class Meta:
        verbose_name = _('Activity Map')
        verbose_name_plural = _('Activity Maps')
        ordering = ('activity',)


class ActivityLink(DateModel):
    activity = models.ForeignKey(verbose_name=_('Activity'), to=Activity)
    link = models.URLField(
        verbose_name=_('Link'), max_length=300, null=True, blank=True
    )

    class Meta:
        verbose_name=_('Activity Link')
        verbose_name_plural=_('Activity Links')


def set_activity_document_upload_path(instance, filename):
    return os.path.join("activity_%d" % instance.activity.id, 'document', filename)


class ActivityDocument(DateModel):
    activity = models.ForeignKey(verbose_name=_('Activity'), to=Activity)
    document = models.FileField(
        verbose_name=_('Document'),upload_to=set_activity_document_upload_path
    )

    class Meta:
        verbose_name=_('Activity Document')
        verbose_name_plural=_('Activity Documents')
