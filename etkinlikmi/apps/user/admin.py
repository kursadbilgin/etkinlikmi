# Standard Library
from copy import deepcopy

# Django
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as _UserAdmin
from django.utils.translation import ugettext_lazy as _

# Local Django
from user.models import User
from user.forms import UserChangeForm

@admin.register(User)
class UserAdmin(_UserAdmin):
    actions = ['delete_selected']

    fieldsets = (
        (_(u'Base Informations'), {
            'fields' : ('email', 'password'),
        }),
        (_(u'Personal Informations'), {
            'fields' : ('first_name', 'last_name', 'city')
        }),
        (_(u'Important Informations'), {
            'fields' : ('last_login',)
        }),
        (_(u'Permissions'), {
            'fields' : ('is_active', 'is_staff', 'is_superuser', 'groups',
                        'user_permissions')
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'city', 'password1',
                        'password2', 'groups', 'user_permissions')}
        ),
    )

    form = UserChangeForm

    list_display = ('first_name', 'last_name', 'city', 'email', 'is_active',
                    'is_superuser', 'is_staff')
    list_filter = ('is_active', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    readonly_fields = ('last_login',)
    ordering = ('first_name', 'last_name')
