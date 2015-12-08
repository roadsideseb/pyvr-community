# -*- coding: utf-8 -*-
from django.contrib import admin

from . import models


@admin.register(models.Company)
class ModelAdmin(admin.ModelAdmin):
    readonly_fields = ('uuid',)
    list_display = ('name', 'website')
    search_fields = ('name',)
