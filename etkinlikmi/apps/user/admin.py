# Standard Library
from copy import deepcopy

# Django
from django.contrib import admin
from django.contrib.auth.models import Group
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.admin import UserAdmin as _UserAdmin

# Local Django
from user.models import User
from user.forms import UserChangeForm
from core.variables import GROUP_DEFAULT

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
                        'password2')}
        ),
    )

    form = UserChangeForm

    list_display = ('first_name', 'last_name', 'city', 'email', 'is_active',
                    'is_superuser', 'is_staff')
    list_filter = ('is_active', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    readonly_fields = ('last_login',)
    ordering = ('first_name', 'last_name')

    def save_model(self, request, obj, form, change):
        obj.save()

        try:
            group = Group.objects.get(name=GROUP_DEFAULT)
            group.user_set.add(obj)
        except Group.DoesNotExist:
            pass

    def get_fieldsets(self, request, obj=None):
        fieldsets = super(UserAdmin, self).get_fieldsets(request, obj)

        custom_fieldsets = deepcopy(fieldsets)

        if not request.user.is_superuser:
            exclude_fieldsets = [ _('Permissions'), _('Groups')]

            custom_fieldsets = [
                field for field in custom_fieldsets if field[0] not in exclude_fieldsets
            ]

        return custom_fieldsets

    def get_queryset(self, request):
        qs = super(UserAdmin, self).get_queryset(request)

        if not request.user.is_superuser:
            qs = qs.filter(pk=request.user.id)

        return qs

    def delete_selected(self, request, obj):
        for user in obj.all():
            if not user.is_superuser:
                user.delete()

    delete_selected.short_description = _("Delete selected Users")

    def get_actions(self, request):
        actions = super(UserAdmin, self).get_actions(request)

        if not request.user.is_superuser:
            del actions['delete_selected']

        return actions

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        else:
            return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        else:
            return False
