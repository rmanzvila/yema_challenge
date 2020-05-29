# -*- coding: utf-8 -*-

import factory
from faker import Factory

from datetime import datetime
from django.utils.timezone import utc

from apps.appointment.models import Doctor, Appointment

fake = Factory.create()


class AppointmentFactory(factory.DjangoModelFactory):
    comments = factory.LazyFunction(fake.text)
    appointment_time = datetime.utcnow().replace(tzinfo=utc)

    class Meta:
        model = Appointment
