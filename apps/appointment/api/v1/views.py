# -*- coding: utf-8 -*-

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_api_key.permissions import HasAPIKey

from apps.appointment.api.v1.forms import AppointmentForm, AppointmentCompleteForm
from apps.appointment.api.v1.selectors import *
from apps.appointment.api.v1.serializers import *
from apps.appointment.api.v1.service import AppointmentService, PatientService, ApiKeyService
from apps.contrib.api.responses import ErrorResponse


class ApiKeyView(APIView):
    permission_classes = []

    def get(self, request):
        """GET /api/v1/access/"""
        api_key = ApiKeyService.generate_key()
        return Response(ApiKeySerializer(api_key, many=False).data)


class DoctorView(APIView):
    """Process the requests for doctors."""
    permission_classes = [HasAPIKey]

    def get(self, request):
        """GET /api/v1/doctors/"""
        doctors = DoctorSelector.get_all()
        return Response(DoctorSerializer(doctors, many=True).data)


class AppointmentView(APIView):
    """Process the requests for appointment."""
    permission_classes = [HasAPIKey]

    def get(self, request):
        """GET /api/v1/appointments/"""
        appointments = AppointmentSelector.get_all()
        return Response(AppointmentSerializer(appointments, many=True).data)

    def post(self, request):
        """POST /api/v1/appointments/"""
        form = AppointmentForm(request.data)
        if not form.is_valid():
            return ErrorResponse('api.appointment.invalid_input', form.errors)

        appointment = AppointmentService.create_appointment(
            form.data['doctor'], form.data['patient'], form.data['appointment_time'], form.data['comments']
        )
        return Response(AppointmentSerializer(appointment, many=False).data)


class AppointmentCompleteView(APIView):
    """Process the requests for appointment."""
    permission_classes = [HasAPIKey]

    def post(self, request):
        """POST /api/v1/appointments/register"""
        form = AppointmentCompleteForm(request.data)
        if not form.is_valid():
            return ErrorResponse('api.appointment.invalid_input', form.errors)

        patient = PatientService.create_patient(
            form.data['name'], form.data['last_name'], form.data['email']
        )
        appointment = AppointmentService.create_appointment(
            form.data['doctor'], patient.uuid, form.data['appointment_time'], form.data['comments']
        )
        return Response(AppointmentSerializer(appointment, many=False).data)


class PatientView(APIView):
    """Process the requests for patients."""
    permission_classes = [HasAPIKey]

    def get(self, request):
        """GET /api/v1/patients/"""
        appointments = PatientSelector.get_all()
        return Response(PatientSerializer(appointments, many=True).data)