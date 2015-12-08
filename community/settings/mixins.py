# -*- coding: utf-8 -*-
import copy


class DjangoLoggingMixin(object):
    FORMATTERS = {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'  # noqa
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    }
    FILTERS = {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        }
    }

    HANDLERS = {
        'sentry': {
            'level': 'ERROR',
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',  # noqa
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    }
    LOGGERS = {
        'django.request': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': False,
        },
        'management_commands': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': False,
        },
        'raven': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
    }

    # Specify the project specific loggers as a simple list if no specific
    # handling of
    PROJECT_LOGGERS = []

    PROJECT_LOGGER_DEFAULT = {
        'level': 'INFO',
        'handlers': ['console'],
        'propagate': False,
    }

    def get_project_loggers(self):
        loggers = []
        for logger in self.PROJECT_LOGGERS:
            # we assume that a dictionary means the logger has already been
            # defined. This allows to override the default logger setting
            if issubclass(logger, dict):
                loggers.update(logger)
                continue

            loggers.update({
                logger: copy.deepcopy(self.PROJECT_LOGGER_DEFAULT)})
        return loggers

    @property
    def LOGGING(self):
        loggers = {}
        loggers.update(self.LOGGERS)
        loggers.update(self.get_project_loggers())
        return {
            'version': 1,
            'disable_existing_logger': False,
            'formatters': self.FORMATTERS,
            'filters': self.FILTERS,
            'handlers': self.HANDLERS,
            'loggers': loggers}


class SecureMixin(object):
    SECURE_SSL_REDIRECT = True
    SECURE_FRAME_DENY = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"
