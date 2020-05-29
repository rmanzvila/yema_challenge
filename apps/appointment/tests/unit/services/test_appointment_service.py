# -*- coding: utf-8 -*-

from django.test import TestCase

import pytest

from apps.appointment.api.v1.service import AppointmentService
from apps.appointment.tests.factories.doctor import DoctorFactory
from apps.appointment.tests.factories.patient import PatientFactory
from datetime import datetime
from django.utils.timezone import utc

@pytest.mark.django_db
class AppointmentServiceTests(TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.doctor = DoctorFactory()
        self.patient = PatientFactory()

    def test_create_appointment(self):
        comments = 'comments'
        time_now = datetime.utcnow().replace(tzinfo=utc)
        appointment = AppointmentService.create_appointment(
            self.doctor.uuid, self.patient.uuid, time_now, comments
        )

        self.assertEqual(appointment.doctor.name, self.doctor.name)
        self.assertEqual(appointment.doctor.last_name, self.doctor.last_name)
        self.assertEqual(appointment.doctor.email, self.doctor.email)
        self.assertEqual(appointment.patient.name, self.patient.name)
        self.assertEqual(appointment.patient.last_name, self.patient.last_name)
        self.assertEqual(appointment.patient.email, self.patient.email)
        self.assertEqual(appointment.comments, comments)
        self.assertEqual(appointment.appointment_time, time_now)
