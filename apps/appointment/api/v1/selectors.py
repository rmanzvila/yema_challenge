# -*- coding: utf-8 -*-

from apps.appointment.models import Doctor, Appointment, Patient


class DoctorSelector(object):
    """Reflects all reading queries over doctors."""

    @classmethod
    def get_all(cls):
        return Doctor.objects.all()


class AppointmentSelector(object):
    """Reflects all reading queries over appointments."""
    @classmethod
    def get_all(cls):
        return Appointment.objects.all()


class PatientSelector(object):
    """Reflects all reading queries over appointments."""
    @classmethod
    def get_all(cls):
        return Patient.objects.all()
