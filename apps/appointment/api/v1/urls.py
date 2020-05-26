# -*- coding: utf-8 -*-

from django.urls import path

from apps.appointment.api.v1.views import *

app_name = 'appointment'
urlpatterns = [
    path('doctors/', DoctorView.as_view(), name='doctor-list'),
    path('appointments/', AppointmentView.as_view(), name='appointment-list'),
    path('appointments/register/', AppointmentCompleteView.as_view(), name='appointment-register'),
    path('patients/', PatientView.as_view(), name='patient-list')
]
