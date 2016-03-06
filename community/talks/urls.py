from django.conf.urls import include, url
from django.views.generic import TemplateView

from . import views


urlpatterns = [
    url(r'^speakers/$', views.SpeakerList.as_view(), name='speaker-list'),
    url(r'^talks/$', views.TalkList.as_view(), name='talk-list'),
]
