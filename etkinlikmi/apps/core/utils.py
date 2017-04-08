# Django
from django.db.models import Q
from django.contrib.auth.models import Permission, Group

# Local Django
from core.variables import GROUP_DEFAULT


def create_group(group_name, permissions):
    try:
        group = Group.objects.get(name=group_name)

        group.permissions.clear()
        group.permissions.add(*permissions)
    except Group.DoesNotExist:
        group = Group.objects.create(name=group_name)
        group.permissions.add(*permissions)


def default():
    user_permissions = [
        p for p in Permission.objects.filter(
            Q(content_type__app_label__in=['user'])
            & Q(codename__icontains='user')
        )
    ]

    activity_permissions = [
        p for p in Permission.objects.filter(
            Q(content_type__app_label__in=['activity'])
        )
    ]

    create_group(GROUP_DEFAULT, (user_permissions + activity_permissions))
