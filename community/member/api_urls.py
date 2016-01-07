# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import api


urlpatterns = [
    url(r'api/members/$', api.MemberList.as_view(), name='member-list'),
]
