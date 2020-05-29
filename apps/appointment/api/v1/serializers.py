# -*- coding: utf-8 -*-
from rest_framework import serializers

from apps.appointment.models import *


class ApiKeySerializer(serializers.Serializer):
    """Helps to print the api key info."""
    api_key = serializers.CharField()


class DoctorSerializer(serializers.ModelSerializer):
    """Helps to print the doctor info."""
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Doctor
        fields = (
            'uuid',
            'name',
            'last_name',
            'email',
            'full_name'
        )

    def get_full_name(self, obj):
        return '{0} {1}'.format(obj.name, obj.last_name)


class PatientSerializer(serializers.ModelSerializer):
    """Helps to print the patient info."""
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Patient
        fields = (
            'uuid',
            'name',
            'last_name',
            'email',
            'full_name'
        )

    def get_full_name(self, obj):
        return '{0} {1}'.format(obj.name, obj.last_name)


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