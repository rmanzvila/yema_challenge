# -*- coding: utf-8 -*-

from rest_framework import status as status_code
from rest_framework.response import Response


class ErrorResponse(Response):

    def __init__(self, code: str, message: str, error_status_code=status_code.HTTP_400_BAD_REQUEST):
        data = {
            'code': code,
            'message': message
        }
        super(ErrorResponse, self).__init__(data=data, status=error_status_code)
