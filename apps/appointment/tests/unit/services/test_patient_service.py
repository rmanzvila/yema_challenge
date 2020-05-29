# -*- coding: utf-8 -*-

from django.test import TestCase

import pytest

from apps.appointment.api.v1.service import AppointmentService, PatientService
from apps.appointment.models import Appointment
from apps.appointment.tests.factories.doctor import DoctorFactory
from apps.appointment.tests.factories.patient import PatientFactory
from datetime import datetime
from django.utils.timezone import utc

from faker import Factory
fake = Factory.create()


@pytest.mark.django_db
class PatientServiceTests(TestCase):

    def test_create_patient(self):
        name = fake.name()
        last_name = fake.word()
        email = fake.email()
        patient = PatientService.create_patient(name, last_name, email)

        self.assertEqual(patient.name, name)
        self.assertEqual(patient.last_name, last_name)
        self.assertEqual(patient.email, email)
