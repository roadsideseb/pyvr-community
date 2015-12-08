# -*- coding: utf-8 -*-
import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Company(models.Model):
    uuid = models.UUIDField(_('uuid'), default=uuid.uuid4, unique=True)
    name = models.CharField(_('name'), max_length=300)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('company')
        verbose_name_plural = _('companies')
