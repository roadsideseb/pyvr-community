# -*- coding: utf-8 -*-
from . base import Base


class CI(Base):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'test_db',
            'USER': 'test_app',
            'PASSWORD': 'testpassword',
            'HOST': '',
            'PORT': ''}}
