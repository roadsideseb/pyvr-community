# -*- coding: utf-8 -*-
import uuid

from urllib.parse import urlparse

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.functional import cached_property
from django.contrib.postgres.fields import JSONField, ArrayField


class SocialLink(models.Model):
    TWITTER = 'twitter'
    LINKEDIN = 'linkedin'
    FACEBOOK = 'facebook'
    GITHUB = 'github'
    BITBUCKET = 'bitbucket'

    SITES = (
        (TWITTER, _('Twitter')),
        (LINKEDIN, _('LinkeIn')),
        (FACEBOOK, _('Facebook')),
        (GITHUB, _('Github')),
        (BITBUCKET, _('Bitbucket')),
    )

    site = models.CharField(_('site'), max_length=100, choices=SITES)
    url = models.URLField(_('URL'))

    @classmethod
    def get_site_from_url(cls, url):
        hostname = urlparse(url).hostname
        try:
            name = hostname.split('.')[-2]
        except (AttributeError, TypeError):
            return None
        if name in [s for s, __ in cls.SITES]:
            return name
        return None

    def __str__(self):
        return self.url

    class Meta:
        verbose_name = _('social link')
        verbose_name_plural = _('social links')


class MeetupUser(models.Model):
    name = models.CharField(_('name'), max_length=300)
    meetup_id = models.CharField(_('meetup ID'), max_length=50, unique=True)

    location = models.CharField(_('location'), max_length=200, blank=True)
    bio = models.TextField(_('bio'), blank=True)

    last_attended_at = models.DateField(_('last attended at'),
                                        null=True,
                                        blank=True)

    groups = ArrayField(models.CharField(max_length=50),
                        verbose_name=_('groups'))

    social_links = models.ManyToManyField('SocialLink',
                                          verbose_name=_('social links'),
                                          related_name='meetup_users')

    raw_data = JSONField(_('meetup metadata'), default=dict)

    def get_meetup_page(self, group):
        return 'http://www.meetup.com/{group}/members/{id}/'.format(
            group=group, id=self.meetup_id)

    def __str__(self):
        return "{u.name} ({u.meetup_id})".format(u=self)

    class Meta:
        verbose_name = _('meetup user')
        verbose_name_plural = _('meetup users')


class Member(models.Model):
    uuid = models.UUIDField(_('uuid'), default=uuid.uuid4)
    name = models.CharField(_('name'), max_length=300)

    email = models.EmailField(_('email'), blank=True)
    twitter = models.CharField(_('twitter handle'), max_length=15, blank=True)
    github = models.CharField(_('github handle'), max_length=100, blank=True)

    linkedin = models.URLField(_('LinkeIn URL'), blank=True)

    is_speaker = models.BooleanField(_('is speaker'), default=False)

    current_position = models.CharField(_('current position'),
                                        max_length=400,
                                        blank=True)

    meetup_user = models.OneToOneField('MeetupUser',
                                       verbose_name=_('meetup user'),
                                       related_name='member',
                                       null=True,
                                       blank=True)

    company = models.ForeignKey('company.Company',
                                verbose_name=_('company'),
                                related_name='employees',
                                null=True,
                                blank=True)

    notes = models.TextField(_('notes'), blank=True)
    tags = ArrayField(models.CharField(max_length=50),
                      verbose_name=_('tags'),
                      default=list,
                      blank=True)

    def __str__(self):
        return self.name

    @cached_property
    def proposed_talks(self):
        return self.talks.all().filter(event__date=None)

    @cached_property
    def presented_talks(self):
        return self.talks.all().exclude(event__date=None)

    class Meta:
        verbose_name = _('member')
        verbose_name_plural = _('members')
