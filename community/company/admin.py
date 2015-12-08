# -*- coding: utf-8 -*-
from django.contrib import admin

from . import models


@admin.register(models.Company)
class ModelAdmin(admin.ModelAdmin):
    read_only_fields = ('uuid',)
    list_display = ('name',)
