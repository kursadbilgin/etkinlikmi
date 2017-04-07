# Django
from django import forms
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

# Local Django
from core.models import City
from activity.models import Activity, ActivityLink, ActivityDocument, ActivityAddress


class ActivityLinkInline(admin.StackedInline):
    model = ActivityLink
    extra = 0
    min_num = 0
    verbose_name = _('Link')
    verbose_name_plural = _('Links')


class ActivityDocumentInline(admin.StackedInline):
    model = ActivityDocument
    extra = 0
    min_num = 0
    verbose_name = _('Document')
    verbose_name_plural = _('Documents')


class ActivityAddressInline(admin.StackedInline):
    model = ActivityAddress
    extra = 0
    min_num = 0
    verbose_name = _('Address')
    verbose_name_plural = _('Addresses')


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    inlines = [ActivityAddressInline, ActivityLinkInline, ActivityDocumentInline]

    fieldsets = (
        (_(u'Base Information'), {
            'fields' : ('user', 'kind', 'name'),
        }),
        (_(u'Date and Time Information'), {
            'fields' : (('starting_date', 'end_date'), ('starting_time', 'end_time'))
        }),
        (_(u'Wage Status Information'), {
            'fields' : ('wage_status',)
        }),
        (_(u'City Information'), {
            'fields' : ('cities',)
        }),
        (_(u'Image'), {
            'fields' : ('image',)
        }),
        (_(u'Statement'), {
            'fields' : ('statement',)
        }),
    )


    list_display = ('name', 'kind', 'starting_date', 'get_cities', 'wage_status')
    list_filter = ('kind', 'starting_date', 'wage_status')
    search_fields = ('kind', 'name', 'kind')
