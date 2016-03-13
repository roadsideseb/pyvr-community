from django.db import models
from django.utils.translation import ugettext_lazy as _

from django_extensions.db.fields import AutoSlugField


class Event(models.Model):
    name = models.CharField(_('name'), max_length=500)
    slug = AutoSlugField(_('slug'), populate_from='name')

    date = models.DateField(_('date'), null=True, blank=True)

    venue = models.ForeignKey('Venue',
                              verbose_name=_('venue'),
                              related_name='events',
                              on_delete=models.SET_NULL,
                              null=True,
                              blank=True)

    venue_options = models.ManyToManyField('Venue',
                                           verbose_name=_('venue options'),
                                           through='Proposal',
                                           related_name='+')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('event')
        verbose_name_plural = _('events')
        ordering = ('-date', 'name')


class Proposal(models.Model):
    """
    A proposal for using a venue for a specific event.
    """
    venue = models.ForeignKey('Venue',
                              verbose_name=_('venue'),
                              related_name='proposals',
                              on_delete=models.SET_NULL,
                              null=True)

    event = models.ForeignKey('Event',
                              verbose_name=_('event'),
                              related_name='proposals',
                              on_delete=models.SET_NULL,
                              null=True)

    date = models.DateField(_('date'), null=True)

    total_cost = models.DecimalField(_('total cost'),
                                     max_digits=12,
                                     decimal_places=2)

    class Meta:
        verbose_name = _('proposal')
        verbose_name_plural = _('proposal')


class Venue(models.Model):
    """
    Representation of a Venue that can be used for an event.
    """
    name = models.CharField(_('name'), max_length=500)
    slug = AutoSlugField(_('slug'), populate_from='name')

    capacity = models.CharField(_('capacity'), max_length=200, blank=True)

    contact = models.TextField(_('contact'), blank=True)
    notes = models.TextField(_('notes'), blank=True)

    class Meta:
        verbose_name = _('venue')
        verbose_name_plural = _('venues')
