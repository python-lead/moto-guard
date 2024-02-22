import logging
import os

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
from sentry_sdk.integrations.logging import LoggingIntegration
from src.settings import ENVIRONMENT
from src.settings.components.base import DEBUG

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "DEBUG",
    },
    "loggers": {
        "faker": {
            "handlers": ["console"],
            "level": "INFO",
        },
    },
}

if not DEBUG:
    sentry_logging = LoggingIntegration(level=logging.INFO, event_level=logging.ERROR)

    sentry_sdk.init(
        dsn=os.environ.get("SENTRY_DSN", None),
        environment=ENVIRONMENT,
        integrations=[DjangoIntegration()],
        traces_sample_rate=1.0,
    )
