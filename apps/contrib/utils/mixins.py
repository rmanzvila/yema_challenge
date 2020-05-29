# -*- coding: utf-8 -*-
import time
import uuid
from django.db import models
from django.utils.translation import ugettext_lazy as _
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework_api_key.models import APIKey


class UUIDPrimaryKeyModelMixin(models.Model):
    """An abstract base class model that provides an uuid field that is the primary key."""

    uuid = models.UUIDField(
        verbose_name='UUID',
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    class Meta:
        abstract = True


class TimeStampedModelMixin(models.Model):
    """Timestamp extra field."""

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated at'))

    class Meta:
        abstract = True
        ordering = ['-created_at', '-updated_at']


class BaseAPITestCase(APITestCase):

    def setUp(self):
        super(APITestCase, self).setUp()

        self.client = APIClient()
        self.auth_client = APIClient()
        self.failed_client = APIClient()

    def generate_authentication(self):
        api_key, key = APIKey.objects.create_key(name="generated-api-key")
        self.auth_client.credentials(
            HTTP_AUTHORIZATION='Api-Key {0}'.format(key),
        )

    def get(self, url=None, data=None, **extra):
        self.generate_authentication()
        return self.auth_client.get(path=url, data=data, **extra)

    def simple_get(self, url=None, data=None, **extra):
        return self.client.get(path=url, data=data, **extra)

    def post(self, url=None, data=None, format=None, content_type=None, **params):
        self.generate_authentication()
        kwargs = self._make_request_kwargs(url, data, format, content_type)
        return self.auth_client.post(**kwargs, **params)

    @classmethod
    def _make_request_kwargs(cls, path, data, format, content_type):
        return {'path': path, 'data': data, 'format': format, 'content_type': content_type}

    def assertBadRequest(self, response):
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def assertUnauthorized(self, response):
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def assertOk(self, response):
        self.assertEqual(response.status_code, status.HTTP_200_OK)
