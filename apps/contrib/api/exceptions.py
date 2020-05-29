# -*- coding: utf-8 -*-


from django.utils.translation import ugettext_lazy as _
from rest_framework import status
from rest_framework.views import exception_handler
from rest_framework.exceptions import (APIException, NotAuthenticated)
from rest_framework_simplejwt.exceptions import (AuthenticationFailed,
                                                 InvalidToken)

from apps.contrib.response_codes import AUTHENTICATION_FAILED, INVALID_TOKEN


class ServerError(APIException):
    """Internal server API exception."""

    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = _('Server error')
    default_code = 'internal_server_error'


class SimpleJWTExceptionParser(object):

    @classmethod
    def parse(cls, exc):
        new_exc = exc
        if isinstance(exc, InvalidToken):
            new_exc = NotAuthenticated(**INVALID_TOKEN)
        elif isinstance(exc, AuthenticationFailed):
            new_exc = NotAuthenticated(**AUTHENTICATION_FAILED)
        return NotAuthenticated(**AUTHENTICATION_FAILED)


def formatted_exception_handler(exc, context):
    """Returns custom formatted response for each exception."""

    exc = SimpleJWTExceptionParser.parse(exc)

    response = exception_handler(exc, context)
    if response is not None:
        response.data = exc.get_full_details()  # noqa: WPS110
    return response
