# -*- coding: utf-8 -*-
from rest_framework import serializers

from apps.appointment.models import Doctor, Appointment, Patient


class DoctorSerializer(serializers.ModelSerializer):
    """Helps to print the doctor info."""

    class Meta:
        model = Doctor
        fields = (
            'uuid',
            'name',
            'last_name',
            'email',
        )


class PatientSerializer(serializers.ModelSerializer):
    """Helps to print the patient info."""

    class Meta:
        model = Patient
        fields = (
            'uuid',
            'name',
            'last_name',
            'email',
            'age',
        )


class AppointmentSerializer(serializers.ModelSerializer):
    """Helps to print the appointment info."""

    class Meta:
        model = Appointment
        fields = (
            'uuid',
            'doctor',
            'patient',
            'appointment_time',
            'comments',
        )

    doctor = DoctorSerializer(many=False)
    patient = PatientSerializer(many=False)