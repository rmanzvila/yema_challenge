# -*- coding: utf-8 -*-
import pytest
from django.utils.translation import ugettext_lazy as _
from doubles.unittest import TestCase

from apps.appointment.models import Doctor, Patient
from apps.appointment.tests.factories.doctor import DoctorFactory
from apps.appointment.tests.factories.patient import PatientFactory


@pytest.mark.django_db
class PatientModelTests(TestCase):

    def setUp(self):
        self.patient = PatientFactory()

    def test_string_representation(self):
        self.assertEqual(str(self.patient), '{0} {1} {2}'.format(
            self.patient.name, self.patient.last_name, self.patient.email))

    def test_verbose_name(self):
        self.assertEqual(str(Patient._meta.verbose_name),
                         _('Patient'))

    def test_verbose_name_plural(self):
        self.assertEqual(str(Patient._meta.verbose_name_plural),
                         _('Patients'))
