# -*- coding: utf-8 -*-

"""Django development settings.

This file contains all the settings that defines the development server.
SECURITY WARNING: don't run with debug turned on in production!
"""
import os
import socket
from typing import List

from config.settings.components import env
from config.settings.components.common import INSTALLED_APPS, TEMPLATES

DEBUG = False

ALLOWED_HOSTS: List[str] = ['*']
SECRET_KEY = env('DJANGO_SECRET_KEY', default='development_secret_key')

INSTALLED_APPS += (
    'django_extensions',
)
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG



# MAIL SETTINGS
# ------------------------------------------------------------------------------
# EMAIL_HOST, EMAIL_PORT = 'mailhog', 1025  # Work with MailHog
DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL', default='Grow <rmanzvila@gmail.com>')
EMAIL_BACKEND = 'anymail.backends.amazon_ses.EmailBackend'


# DEBUGGING
# ------------------------------------------------------------------------------
INTERNAL_IPS = ['127.0.0.1', '10.0.2.2']  # localhost IP, docker internal IP

# TESTING
# ------------------------------------------------------------------------------
TEST_RUNNER = 'django.test.runner.DiscoverRunner'
