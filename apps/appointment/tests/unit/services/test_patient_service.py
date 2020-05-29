# -*- coding: utf-8 -*-

import pytest
from django.test import TestCase
from faker import Factory

from apps.appointment.api.v1.service import PatientService

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
