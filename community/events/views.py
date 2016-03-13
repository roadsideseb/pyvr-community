from django.views import generic

from braces import views

from . import models


class EventList(views.SuperuserRequiredMixin, generic.ListView):
    model = models.Event
    context_object_name = 'events'
    template_name = 'events/event_list.html'

    def get_queryset(self):
        return self.model.objects.all().order_by('-date')


class VenueList(views.SuperuserRequiredMixin, generic.ListView):
    model = models.Venue
    context_object_name = 'venues'
    template_name = 'events/venue_list.html'

    def get_queryset(self):
        return self.model.objects.all().prefetch_related('proposals')
