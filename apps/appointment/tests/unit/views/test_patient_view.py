# -*- coding: utf-8 -*-

import pytest
from django.urls import reverse
from apps.appointment.tests.factories.patient import PatientFactory
from apps.contrib.utils.mixins import BaseAPITestCase


@pytest.mark.django_db
class PatientViewTests(BaseAPITestCase):

    def setUp(self):
        super().setUp()
        self.patient_1 = PatientFactory()
        self.patient_2 = PatientFactory()
        self.patient_3 = PatientFactory()

    @classmethod
    def make_request_url(cls):
        return reverse('api-appointment:v1:patient-list')

    def test_patient_view(self):
        request_url = self.make_request_url()
        response = self.get(request_url)
        response_data = response.json()
        self.assertOk(response)
        self.assertIsInstance(response_data['response'], list)
        self.assertEquals(set(response_data['response'][0].keys()),
                          {'uuid', 'name', 'last_name', 'email', 'full_name'})

    def test_credentials_required(self):
        request_url = self.make_request_url()
        response = self.simple_get(request_url)
        self.assertUnauthorized(response)
