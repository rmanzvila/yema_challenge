# -*- coding: utf-8 -*-
import datetime

import factory
from faker import Factory


from apps.appointment.models import Doctor, Appointment

fake = Factory.create()


class AppointmentFactory(factory.DjangoModelFactory):
    comments = factory.LazyFunction(fake.text)
    appointment_time = factory.LazyFunction(datetime.datetime.now)

    class Meta:
        model = Appointment
