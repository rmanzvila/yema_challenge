# -*- coding: utf-8 -*-

from datetime import datetime

import factory
from django.utils.timezone import utc
from faker import Factory

from apps.appointment.models import Appointment

fake = Factory.create()


class AppointmentFactory(factory.DjangoModelFactory):
    comments = factory.LazyFunction(fake.text)
    appointment_time = datetime.utcnow().replace(tzinfo=utc)

    class Meta:
        model = Appointment
