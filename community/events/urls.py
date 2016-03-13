from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^events/$', views.EventList.as_view(), name='event-list'),
    url(r'^venues/$', views.VenueList.as_view(), name='venue-list'),
]
