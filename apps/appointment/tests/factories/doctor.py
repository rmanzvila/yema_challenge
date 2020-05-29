# -*- coding: utf-8 -*-
from datetime import time

import factory
from faker import Factory

from apps.appointment.models import Doctor

fake = Factory.create()


class DoctorFactory(factory.DjangoModelFactory):
    name = factory.LazyFunction(fake.first_name)
    last_name = factory.LazyFunction(fake.last_name)
    email = factory.LazyFunction(fake.email)

    class Meta:
        model = Doctor
