# -*- encoding:utf-8 -*-
import pytest
from django.test import TestCase

from apps.appointment.api.v1.serializers import ApiKeySerializer


@pytest.mark.django_db
class ApikeyTestSerializer(TestCase):

    def test_valid_serializer(self):
        serializer = ApiKeySerializer(data={'api_key': 'abcdefghijklmnopqrstuvwxyz'})
        self.assertTrue(serializer.is_valid())

    def test_invalid_serializer(self):
        serializer = ApiKeySerializer(data={})
        self.assertFalse(serializer.is_valid())
