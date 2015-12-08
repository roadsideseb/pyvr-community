# -*- coding: utf-8 -*-
from django.contrib import admin

from . import models


@admin.register(models.Company)
class ModelAdmin(admin.ModelAdmin):
    list_display = ('name',)
