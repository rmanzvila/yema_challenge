import datetime
from datetime import datetime

import pytest
from django.utils.timezone import utc
from django.utils.translation import ugettext_lazy as _
from doubles.unittest import TestCase
from faker import Factory

from apps.appointment.api.v1.forms import AppointmentForm
from apps.appointment.tests.factories.doctor import DoctorFactory
from apps.appointment.tests.factories.patient import PatientFactory

fake = Factory.create()


@pytest.mark.django_db
class AppointmentFormTests(TestCase):

    def setUp(self):
        self.doctor = DoctorFactory()
        self.patient = PatientFactory()

    def test_valid_data(self):
        data = {
            'doctor': self.doctor.uuid,
            'patient': self.patient.uuid,
            'comments': 'comments',
            'appointment_time': datetime.utcnow().replace(tzinfo=utc)
        }
        form = AppointmentForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_data_doctor_not_found(self):
        data = {
            'doctor': fake.uuid4(),
            'patient': self.patient.uuid,
            'comments': 'comments',
            'appointment_time': datetime.utcnow().replace(tzinfo=utc)
        }
        form = AppointmentForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'doctor': [_('Object not found')],
        })

    def test_invalid_data_patient_not_found(self):
        data = {
            'doctor': self.doctor.uuid,
            'patient': fake.uuid4(),
            'comments': 'comments',
            'appointment_time': datetime.utcnow().replace(tzinfo=utc)
        }
        form = AppointmentForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'patient': [_('Object not found')],
        })
