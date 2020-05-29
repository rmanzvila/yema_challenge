# -*- coding: utf-8 -*-

from django.test import TestCase

import pytest

from apps.appointment.api.v1.service import AppointmentService, PatientService, ApiKeyService
from apps.appointment.models import Appointment
from apps.appointment.tests.factories.doctor import DoctorFactory
from apps.appointment.tests.factories.patient import PatientFactory
from datetime import datetime
from django.utils.timezone import utc

from faker import Factory
fake = Factory.create()


@pytest.mark.django_db
class ApiKeyServiceTests(TestCase):

    def test_create_api_key(self):
        api_key = ApiKeyService.generate_key()

        self.assertIsInstance(api_key, dict)
        self.assertEquals(api_key.keys(), {'api_key',})

