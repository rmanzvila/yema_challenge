# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from datetime import datetime

from django.utils.timezone import utc
from rest_framework.renderers import JSONRenderer
from rest_framework.utils.encoders import JSONEncoder


class SafeJSONEncoder(JSONEncoder):
    def encode(self, o):
        # Override JSONEncoder.encode because it has hacks for
        # performance that make things more complicated.
        chunks = self.iterencode(o, True)
        return u''.join(chunks)

    def iterencode(self, o, _one_shot=False):
        chunks = super(SafeJSONEncoder, self).iterencode(o, _one_shot)
        for chunk in chunks:
            chunk = chunk.replace('&', '\\u0026')
            chunk = chunk.replace('<', '\\u003c')
            chunk = chunk.replace('>', '\\u003e')
            yield chunk


class SafeJSONRenderer(JSONRenderer):
    encoder_class = SafeJSONEncoder

    def render(self, data={}, accepted_media_type=None, renderer_context=None):
        data = {
            'response': data,
            'datetime': datetime.utcnow().replace(tzinfo=utc)
        }

        if 'response' in renderer_context:
            data['status'] = renderer_context['response'].status_text

        return super().render(data, accepted_media_type, renderer_context)
