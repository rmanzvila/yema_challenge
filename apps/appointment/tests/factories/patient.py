# -*- coding: utf-8 -*-
from datetime import time

import factory
from faker import Factory

from django.contrib.gis.geos import Point


from apps.appointment.models import Doctor, Patient

fake = Factory.create()


class PatientFactory(factory.DjangoModelFactory):
    name = factory.LazyFunction(fake.first_name)
    last_name = factory.LazyFunction(fake.last_name)
    email = factory.LazyFunction(fake.email)

    class Meta:
        model = Patient
