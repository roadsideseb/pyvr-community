from django.db import models
from django.utils.translation import ugettext_lazy as _


class SpeakerProfile(models.Model):
    full_name = models.CharField(_('name'), max_length=200)

    bio = models.TextField(_('bio'))

    member = models.OneToOneField('member.Member',
                                  verbose_name=_('member'),
                                  related_name='speaker_profile')

    class Meta:
        verbose_name = _('speaker profile')
        verbose_name_plural = _('speaker profile')


class Talk(models.Model):
    title = models.CharField(_('title'), max_length=300)
    summary = models.TextField(_('summary'), blank=True)

    speakers = models.ManyToManyField('member.Member',
                                      verbose_name=_('speaker'),
                                      related_name='talks')

    event = models.ForeignKey('events.Event',
                              verbose_name=_('presented at'),
                              related_name='talks',
                              null=True,
                              blank=True)

    class Meta:
        verbose_name = _('talk')
        verbose_name_plural = _('talks')
