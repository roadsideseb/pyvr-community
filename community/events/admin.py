from django.contrib import admin

from . import models


class ProposalInline(admin.TabularInline):
    model = models.Proposal


@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'date', 'venue')
    inlines = [ProposalInline]


@admin.register(models.Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'capacity')
    inlines = [ProposalInline]
