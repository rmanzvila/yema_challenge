import pytest
from django.test import TestCase

from apps.appointment.api.v1.selectors import Patient, PatientSelector
from apps.appointment.tests.factories.patient import PatientFactory


@pytest.mark.django_db
class DoctorSelectorTests(TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.patient_1 = PatientFactory()
        self.patient_2 = PatientFactory()
        self.patient_3 = PatientFactory()

    def test_get_all_doctors(self):
        patients = PatientSelector.get_all()
        first_patient = patients.filter(email=self.patient_1.email).first()

        self.assertEqual(patients.count(), 3)
        self.assertIsInstance(first_patient, Patient)

        self.assertEqual(first_patient.email, self.patient_1.email)
        self.assertEqual(first_patient.name, self.patient_1.name)
        self.assertEqual(first_patient.last_name, self.patient_1.last_name)
