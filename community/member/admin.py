# -*- coding: utf-8 -*-
from django.contrib import admin

from . import models

@admin.register(models.MeetupUser)
class MeetupUserAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'twitter', 'github')
    search_fields = ('name',)


admin.site.register(models.SocialLink)
