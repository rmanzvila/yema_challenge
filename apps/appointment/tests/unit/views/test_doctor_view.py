# -*- coding: utf-8 -*-

from django.urls import reverse

import pytest
from apps.appointment.tests.factories.doctor import DoctorFactory
from apps.contrib.utils.mixins import BaseAPITestCase


@pytest.mark.django_db
class DoctorViewTests(BaseAPITestCase):

    def setUp(self):
        super().setUp()
        self.doctor_1 = DoctorFactory()
        self.doctor_2 = DoctorFactory()
        self.doctor_3 = DoctorFactory()

    @classmethod
    def make_request_url(cls):
        return reverse('api-appointment:v1:doctor-list')

    def test_doctor_view(self):
        request_url = self.make_request_url()
        response = self.get(request_url)
        response_data = response.json()
        self.assertOk(response)
        self.assertIsInstance(response_data['response'], list)
        self.assertEquals(set(response_data['response'][0].keys()),
                          {'uuid','name','last_name','email','full_name'})

    def test_credentials_required(self):
        request_url = self.make_request_url()
        response = self.simple_get(request_url)
        self.assertUnauthorized(response)
