# Django
from django import forms
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

# Local Django
from core.models import City

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('city',)
    search_fields = ('city',)
