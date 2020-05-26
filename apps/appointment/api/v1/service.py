# -*- encoding:utf-8 -*-

from apps.appointment.models import Appointment


class AppointmentService:

    @classmethod
    def create_appointment(cls, ):
        return Appointment.objects.first()
        appointment = Appointment.objects.create(
        )
        return appointment