# -*- coding: utf-8 -*-
from django.contrib import admin

from . import models


class MemberTagListFilter(admin.SimpleListFilter):
    """This is a list filter based on the values
    from a model's `keywords` ArrayField. """

    title = 'Tags'
    parameter_name = 'tags'

    def lookups(self, request, model_admin):
        # Very similar to our code above, but this method must return a
        # list of tuples: (lookup_value, human-readable value). These
        # appear in the admin's right sidebar

        keywords = models.Member.objects.values_list("tags", flat=True)
        keywords = [(kw, kw) for sublist in keywords for kw in sublist if kw]
        keywords = sorted(set(keywords))
        return keywords

    def queryset(self, request, queryset):
        # when a user clicks on a filter, this method gets called. The
        # provided queryset with be a queryset of Items, so we need to
        # filter that based on the clicked keyword.

        lookup_value = self.value()  # The clicked keyword. It can be None!
        if lookup_value:
            # the __contains lookup expects a list, so...
            queryset = queryset.filter(tags__contains=[lookup_value])
        return queryset


@admin.register(models.MeetupUser)
class MeetupUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    list_filter = ('location',)
    search_fields = ('name',)


@admin.register(models.Member)
class MemberAdmin(admin.ModelAdmin):
    readonly_fields = ('uuid',)
    list_display = ('name', 'email', 'twitter', 'github')
    list_filter = ('completeness_score', 'company', MemberTagListFilter)
    search_fields = ('name',)


admin.site.register(models.SocialLink)
