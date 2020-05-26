# -*- coding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _


INVALID_TOKEN = {
    'code': 'invalid_token',
    'detail': _('This TOKEN is invalid or EXPIRED'),
}


AUTHENTICATION_FAILED = {
    'code': 'authentication_failed',
    'detail': _('The authentication process failed, try again.'),
}