# Django
from django import forms
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

# Local Django
from activity.models import Activity, ActivityLink, ActivityDocument, ActivityMap


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


class ActivityMapInline(admin.StackedInline):
    model = ActivityMap
    extra = 1
    max_num = 1
    verbose_name = _('Map')
    verbose_name_plural = _('Maps')


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    inlines = [ActivityMapInline, ActivityLinkInline, ActivityDocumentInline]

    fieldsets = (
        (_(u'Base Information'), {
            'fields' : ('user', 'kind', 'name', 'date'),
        }),
        (_(u'Address Information'), {
            'fields' : ('city', 'address')
        }),
        (_(u'Image'), {
            'fields' : ('image',)
        }),
        (_(u'Statement'), {
            'fields' : ('statement',)
        }),
    )


    list_display = ('name', 'kind', 'date', 'city')
    list_filter = ('name', 'kind', 'date', 'city')
    search_fields = ('kind', 'name', 'kind')
