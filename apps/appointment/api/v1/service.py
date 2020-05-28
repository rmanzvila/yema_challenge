# -*- encoding:utf-8 -*-

from apps.appointment.models import Appointment, Patient


class AppointmentService:
    """ Provides methods to work with appointments"""
    @classmethod
    def create_appointment(cls, doctor_id: str, patient_id: str, appointment_time, comments: str):
        appointment = Appointment.objects.create(
            doctor_id=doctor_id,
            patient_id=patient_id,
            appointment_time=appointment_time,
            comments=comments
        )
        return appointment


class PatientService:
    """ Provides methods to work with patients"""
    @classmethod
    def create_patient(cls, name: str, last_name: str, email: str):
        patient = Patient.objects.create(
            name=name,
            last_name=last_name,
            email=email,
        )
        return patient
