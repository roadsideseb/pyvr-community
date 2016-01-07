# -*- coding: utf-8 -*-
from __future__ import absolute_import

from configurations import values

from .base import Base


class Production(Base):
    DEBUG = False
    TEMPLATE_DEBUG = False

    STATIC_ROOT = '/app/static'

    EMAIL_SUBJECT_PREFIX = '[community][Prod] '

    INSTALLED_APPS = Base.INSTALLED_APPS + [
        'raven.contrib.django.raven_compat',
    ]

    DATABASES = values.DatabaseURLValue()
    ALLOWED_HOSTS = ['community.pyvr.org', 'pyvr-community.herokuapp.com']

    RAVEN_DSN = values.Value()

    @property
    def RAVEN_CONFIG(self):
        return {'dsn': self.RAVEN_DSN}
