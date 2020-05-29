# -*- encoding:utf-8 -*-
import pytest
from django.test import TestCase
from faker import Factory

from apps.appointment.api.v1.serializers import PatientSerializer

fake = Factory.create()


@pytest.mark.django_db
class PatientTestSerializer(TestCase):

    def test_valid_serializer(self):
        name = fake.name()
        last_name = fake.word()
        serializer = PatientSerializer(data={
            'uuid': fake.uuid4(), 'name': name, 'last_name': last_name,
            'email': fake.email(), 'full_name': '%s %s'.format(name, last_name)
        })
        self.assertTrue(serializer.is_valid())

    def test_invalid_serializer(self):
        serializer = PatientSerializer(data={})
        self.assertFalse(serializer.is_valid())
