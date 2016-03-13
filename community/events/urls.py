from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^events/$', views.EventList.as_view(), name='event-list'),
]
