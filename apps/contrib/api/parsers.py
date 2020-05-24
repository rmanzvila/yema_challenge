# -*- coding: utf-8 -*-

import json

from rest_framework.parsers import BaseParser


class PlainTextParser(BaseParser):
    """Plain text parser."""

    media_type = 'text/plain'

    def parse(self, stream, media_type=None, parser_context=None):
        """Simply return a string representing the body of the request."""
        return stream.read()


class SNSJsonParser(BaseParser):
    """Plain text parser."""

    media_type = 'text/plain'

    def parse(self, stream, media_type=None, parser_context=None):
        """Simply return a string representing the body of the request."""
        try:
            return json.loads(stream.read())
        except Exception as e:
            return ''
