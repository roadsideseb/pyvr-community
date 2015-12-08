# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    def __unicode__(self):
        return self.username
