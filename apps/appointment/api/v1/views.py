# -*- coding: utf-8 -*-

from rest_framework.views import APIView
from rest_framework.response import Response

from apps.appointment.api.v1.forms import AppointmentForm, AppointmentCompleteForm
from apps.appointment.api.v1.selectors import *
from apps.appointment.api.v1.serializers import *
from apps.appointment.api.v1.service import AppointmentService
from apps.contrib.api.responses import ErrorResponse


class DoctorView(APIView):
    """Process the requests for doctors."""

    #permission_classes = [IsAuthenticated, ]
    permission_classes = []

    def get(self, request):
        """GET /api/v1/doctors/"""
        doctors = DoctorSelector.get_all()
        return Response(DoctorSerializer(doctors, many=True).data)


class AppointmentView(APIView):
    """Process the requests for appointment."""

    #permission_classes = [IsAuthenticated, ]
    permission_classes = []

    def get(self, request):
        """GET /api/v1/appointments/"""
        appointments = AppointmentSelector.get_all()
        return Response(AppointmentSerializer(appointments, many=True).data)

    def post(self, request):
        """POST /api/v1/appointments/"""
        form = AppointmentForm(request.data)
        if not form.is_valid():
            return ErrorResponse('api.appointment.invalid_input', form.errors)

        appointment = AppointmentService.create_appointment()
        return Response(AppointmentSerializer(appointment, many=False).data)


class AppointmentCompleteView(APIView):
    """Process the requests for appointment."""

    #permission_classes = [IsAuthenticated, ]
    permission_classes = []

    def post(self, request):
        """POST /api/v1/appointments/register"""
        form = AppointmentCompleteForm(request.data)
        if not form.is_valid():
            return ErrorResponse('api.appointment.invalid_input', form.errors)

        appointment = AppointmentService.create_appointment()
        return Response(AppointmentSerializer(appointment, many=False).data)


class PatientView(APIView):
    """Process the requests for patients."""

    #permission_classes = [IsAuthenticated, ]
    permission_classes = []

    def get(self, request):
        """GET /api/v1/patients/"""
        appointments = PatientSelector.get_all()
        return Response(PatientSerializer(appointments, many=True).data)