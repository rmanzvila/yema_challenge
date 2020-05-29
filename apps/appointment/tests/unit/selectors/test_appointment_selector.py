# -*- encoding:utf-8 -*-
import pytest
from django.test import TestCase

from apps.appointment.api.v1.selectors import AppointmentSelector
from apps.appointment.models import Appointment
from apps.appointment.tests.factories.appointment import AppointmentFactory
from apps.appointment.tests.factories.doctor import DoctorFactory
from apps.appointment.tests.factories.patient import PatientFactory


@pytest.mark.django_db
class AppointmentSelectorTests(TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.doctor = DoctorFactory()
        self.patient = PatientFactory()
        self.appointment = AppointmentFactory(doctor=self.doctor, patient=self.patient)

    def test_get_all_appointments(self):
        appointments = AppointmentSelector.get_all()
        first_appointment = appointments.first()

        self.assertEqual(appointments.count(), 1)
        self.assertIsInstance(first_appointment, Appointment)

        self.assertEqual(first_appointment.doctor.name, self.doctor.name)
        self.assertEqual(first_appointment.doctor.last_name, self.doctor.last_name)
        self.assertEqual(first_appointment.doctor.email, self.doctor.email)
        self.assertEqual(first_appointment.patient.name, self.patient.name)
        self.assertEqual(first_appointment.patient.last_name, self.patient.last_name)
        self.assertEqual(first_appointment.patient.email, self.patient.email)
