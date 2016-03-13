# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib import admin
from django.conf.urls import include, url
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),

    url(r'^', include('community.users.urls', namespace='users')),
    url(r'^', include('community.talks.urls', namespace='talks')),
    url(r'^', include('community.events.urls', namespace='events')),

    url(r'^admin/', include(admin.site.urls)),
]


if settings.DEBUG:
    # Render statics/media locally
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    # Do explicit setup of django debug toolbar
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls))]
