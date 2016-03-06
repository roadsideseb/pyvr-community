from django.contrib import admin

from . import models


@admin.register(models.SpeakerProfile)
class SpeakerProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'member')


@admin.register(models.Talk)
class TalkAdmin(admin.ModelAdmin):
    list_display = ('title',)
    raw_id_fields = ('speakers',)
