from datetime import datetime

from django.contrib import messages
from django.contrib.admin.sites import AdminSite
from django.test import TestCase
from django.utils.timezone import utc
from doubles import allow

from apps.appointment.admin import AppointmentAdmin
from apps.appointment.models import Appointment
from apps.appointment.tests.factories.appointment import AppointmentFactory
from apps.appointment.tests.factories.doctor import DoctorFactory
from apps.appointment.tests.factories.patient import PatientFactory


class MockRequest(object):
    pass


request = MockRequest()


class AppAdminTest(TestCase):

    def setUp(self):
        self.doctor = DoctorFactory()
        self.patient = PatientFactory()
        self.appointment = AppointmentFactory(doctor=self.doctor, patient=self.patient)
        self.app_admin = AppointmentAdmin(Appointment, AdminSite())

    def test_send_email(self):
        (allow(messages).info.and_return(None))
        queryset = Appointment.objects.all()
        self.app_admin.send_by_email(request, queryset)

    def test_get_doctor_name(self):
        name = self.app_admin.get_doctor_name(self.appointment)

        self.assertIsInstance(name, str)
        self.assertEqual(name, '{0} {1}'.format(
            self.appointment.doctor.name, self.appointment.doctor.last_name))

    def test_get_patient_name(self):
        name = self.app_admin.get_patient_name(self.appointment)

        self.assertIsInstance(name, str)
        self.assertEqual(name, '{0} {1}'.format(
            self.appointment.patient.name, self.appointment.patient.last_name))
