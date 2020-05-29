# -*- coding: utf-8 -*-

import pytest
from django.urls import reverse

from apps.appointment.models import Appointment, Patient
from apps.appointment.tests.factories.appointment import AppointmentFactory
from apps.appointment.tests.factories.doctor import DoctorFactory
from apps.appointment.tests.factories.patient import PatientFactory
from apps.contrib.utils.mixins import BaseAPITestCase


@pytest.mark.django_db
class PatientViewTests(BaseAPITestCase):

    def setUp(self):
        super().setUp()
        self.patient = PatientFactory()
        self.doctor = DoctorFactory()
        self.appointment = AppointmentFactory(doctor=self.doctor, patient=self.patient)
        self.appointment_1 = AppointmentFactory(doctor=self.doctor, patient=self.patient)

    @classmethod
    def make_request_url(cls):
        return reverse('api-appointment:v1:appointment-list')

    @classmethod
    def make_request_url_register(cls):
        return reverse('api-appointment:v1:appointment-register')

    @classmethod
    def make_payload(cls, doctor, patient):
        return {
            'doctor': doctor.uuid,
            'patient': patient.uuid,
            'appointment_time': '2020-05-25 13:41:38',
            'comments': 'comments about patient'
        }

    @classmethod
    def make_payload_for_register(cls, doctor):
        return {
            'doctor': doctor.uuid,
	        'name': 'Ricardo',
            'last_name': 'Manzanares Avila',
            'email': 'rmanzvila@gmail.com',
            'appointment_time': '2020-05-25 13:41:38',
            'comments': 'comments about patient'
        }

    def test_patient_view(self):
        request_url = self.make_request_url()
        response = self.get(request_url)
        response_data = response.json()
        self.assertOk(response)
        self.assertIsInstance(response_data['response'], list)
        self.assertEquals(set(response_data['response'][0].keys()),
                          {'uuid', 'doctor', 'patient', 'appointment_time', 'comments'})

    def test_credentials_required_on_patient(self):
        request_url = self.make_request_url()
        response = self.simple_get(request_url)
        self.assertUnauthorized(response)

    def test_patient_view_post(self):
        request_url = self.make_request_url()
        response = self.post(request_url, data=self.make_payload(self.doctor, self.patient))
        response_data = response.json()
        self.assertOk(response)
        self.assertEqual(Patient.objects.count(), 1)
        self.assertEqual(Appointment.objects.count(), 3)
        self.assertEquals(set(response_data['response'].keys()),
                          {'uuid', 'doctor', 'patient', 'appointment_time', 'comments'})

    def test_patient_view_post_incorrect(self):
        request_url = self.make_request_url()
        response = self.post(request_url, data={})
        _response_data = response.json()
        self.assertBadRequest(response)
        self.assertEqual(Appointment.objects.count(), 2)

    def test_patient_view_register(self):
        request_url = self.make_request_url_register()
        response = self.post(request_url, data=self.make_payload_for_register(self.doctor))
        response_data = response.json()
        self.assertOk(response)
        self.assertEqual(Patient.objects.count(), 2)
        self.assertEqual(Appointment.objects.count(), 3)
        self.assertEquals(set(response_data['response'].keys()),
                          {'uuid', 'doctor', 'patient', 'appointment_time', 'comments'})

    def test_patient_view_post_incorrect_register(self):
        request_url = self.make_request_url_register()
        response = self.post(request_url, data={})
        _response_data = response.json()
        self.assertBadRequest(response)
        self.assertEqual(Appointment.objects.count(), 2)
