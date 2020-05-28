# -*- coding: utf-8 -*-

# Caching
# https://docs.djangoproject.com/en/2.2/topics/cache/
from config.settings.components import env

REDIS_CACHE_URL = env('REDIS_CACHE_URL', default='redis://redis:6379/0')

# CACHE CONFIGURATION
# ------------------------------------------------------------------------------
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache'
    }
}
