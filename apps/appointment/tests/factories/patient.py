# -*- coding: utf-8 -*-
import factory
from faker import Factory
from apps.appointment.models import Patient

fake = Factory.create()


class PatientFactory(factory.DjangoModelFactory):
    name = factory.LazyFunction(fake.first_name)
    last_name = factory.LazyFunction(fake.last_name)
    email = factory.LazyFunction(fake.email)

    class Meta:
        model = Patient
