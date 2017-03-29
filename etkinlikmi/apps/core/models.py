# Django
from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _


class DateModel(models.Model):
    create_date = models.DateTimeField(verbose_name=_('Create Date'), auto_now_add=True, editable=False)
    update_date = models.DateTimeField(verbose_name=_('Update Date'), auto_now=True, editable=False)

    class Meta:
        abstract = True


class City(models.Model):
    city = models.CharField(verbose_name=_('City'), max_length=55, unique=True)

    class Meta:
        verbose_name=_(u'City')
        verbose_name_plural=_(u'Cities')

    def __str__(self):
        return self.city
