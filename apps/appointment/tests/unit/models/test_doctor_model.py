# -*- coding: utf-8 -*-
import pytest
from django.utils.translation import ugettext_lazy as _
from doubles.unittest import TestCase

from apps.appointment.models import Doctor
from apps.appointment.tests.factories.doctor import DoctorFactory


@pytest.mark.django_db
class DoctorModelTests(TestCase):

    def setUp(self):
        self.doctor = DoctorFactory()

    def test_string_representation(self):
        self.assertEqual(str(self.doctor), '{0} {1} {2}'.format(
            self.doctor.name, self.doctor.last_name, self.doctor.email))

    def test_verbose_name(self):
        self.assertEqual(str(Doctor._meta.verbose_name),
                         _('Doctor'))

    def test_verbose_name_plural(self):
        self.assertEqual(str(Doctor._meta.verbose_name_plural),
                         _('Doctors'))
