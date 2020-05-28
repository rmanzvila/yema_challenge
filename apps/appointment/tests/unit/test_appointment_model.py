# -*- coding: utf-8 -*-
import pytest

from doubles.unittest import TestCase

from apps.appointment.models import Doctor, Patient, Appointment
from apps.appointment.tests.factories.appointment import AppointmentFactory
from apps.appointment.tests.factories.doctor import DoctorFactory
from django.utils.translation import ugettext_lazy as _

from apps.appointment.tests.factories.patient import PatientFactory


@pytest.mark.django_db
class AppointmentModelTests(TestCase):

    def setUp(self):
        self.doctor = DoctorFactory()
        self.patient = PatientFactory()
        self.appointment = AppointmentFactory(doctor=self.doctor, patient=self.patient)

    def test_string_representation(self):
        self.assertEqual(str(self.appointment),'{0} {1} - {2}'.format(
            self.patient.name, self.patient.last_name, self.doctor.email))

    def test_verbose_name(self):
        self.assertEqual(str(Appointment._meta.verbose_name),
                         _('Appointment'))

    def test_verbose_name_plural(self):
        self.assertEqual(str(Appointment._meta.verbose_name_plural),
                         _('Appointments'))
