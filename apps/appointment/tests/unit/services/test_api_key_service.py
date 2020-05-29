# -*- coding: utf-8 -*-

import pytest
from django.test import TestCase
from faker import Factory

from apps.appointment.api.v1.service import ApiKeyService

fake = Factory.create()


@pytest.mark.django_db
class ApiKeyServiceTests(TestCase):

    def test_create_api_key(self):
        api_key = ApiKeyService.generate_key()

        self.assertIsInstance(api_key, dict)
        self.assertEquals(api_key.keys(), {'api_key',})
