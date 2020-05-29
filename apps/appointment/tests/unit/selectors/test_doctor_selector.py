# -*- encoding:utf-8 -*-

import pytest
from django.test import TestCase

from apps.appointment.api.v1.selectors import DoctorSelector
from apps.appointment.models import Doctor
from apps.appointment.tests.factories.doctor import DoctorFactory


@pytest.mark.django_db
class DoctorSelectorTests(TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.doctor_1 = DoctorFactory()
        self.doctor_2 = DoctorFactory()
        self.doctor_3 = DoctorFactory()

    def test_get_all_doctors(self):
        doctors = DoctorSelector.get_all()
        first_doctor = doctors.filter(email=self.doctor_1.email).first()

        self.assertEqual(doctors.count(), 3)
        self.assertIsInstance(first_doctor, Doctor)

        self.assertEqual(first_doctor.email,self.doctor_1.email)
        self.assertEqual(first_doctor.name,self.doctor_1.name)
        self.assertEqual(first_doctor.last_name,self.doctor_1.last_name)
