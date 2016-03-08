from django.db import models
from django.utils.translation import ugettext_lazy as _

from django_extensions.db.fields import AutoSlugField


class Event(models.Model):
    name = models.CharField(_('name'), max_length=500)
    slug = AutoSlugField(_('slug'), populate_from='name')

    date = models.DateField(_('date'), null=True, blank=True)

    location = models.CharField(_('location'), max_length=500)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('event')
        verbose_name_plural = _('events')
        ordering = ('-date', 'name')
