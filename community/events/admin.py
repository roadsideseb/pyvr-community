from django.contrib import admin

from . import models


@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'date', 'location')
