# -*- coding: utf-8 -*-

import pytest
from django.urls import reverse
from apps.contrib.utils.mixins import BaseAPITestCase


@pytest.mark.django_db
class ApiKeyViewTests(BaseAPITestCase):

    def setUp(self):
        super().setUp()

    @classmethod
    def make_request_url(cls):
        return reverse('api-appointment:v1:api-key-access')

    def test_api_key_view(self):
        request_url = self.make_request_url()
        response = self.simple_get(request_url)
        self.assertOk(response)
