# -*- coding: utf-8 -*-
from django.contrib import admin

from . import models

@admin.register(models.MeetupUser)
class MeetupUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    list_filter = ('location',)
    search_fields = ('name',)


@admin.register(models.Member)
class MemberAdmin(admin.ModelAdmin):
    readonly_fields = ('uuid',)
    list_display = ('name', 'email', 'twitter', 'github')
    list_filter = ('company',)
    search_fields = ('name',)


admin.site.register(models.SocialLink)
