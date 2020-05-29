# -*- encoding:utf-8 -*-
from django import forms
from rest_framework.exceptions import ValidationError

from apps.appointment.models import Doctor, Patient
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


def found_doctor(value):
    """Form validator for doctor uuid"""
    try:
        Doctor.objects.get(uuid=value)
    except Doctor.DoesNotExist:
        raise ValidationError(_('Object not found'))
    return value


def found_patient(value):
    """Form validator for patient uuid"""
    try:
        Patient.objects.get(uuid=value)
    except Patient.DoesNotExist:
        raise ValidationError(_('Object not found'))
    return value


class AppointmentForm(forms.Form):
    """Form to create appointment from created patient."""
    doctor = forms.CharField(required=True, validators=[found_doctor])
    patient = forms.CharField(required=True, validators=[found_patient])
    appointment_time = forms.DateTimeField(required=True)
    comments = forms.CharField(required=False)


class AppointmentCompleteForm(forms.Form):
    """Form to create appointment from not created patient."""
    doctor = forms.CharField(required=True, validators=[found_doctor])
    name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    appointment_time = forms.DateTimeField(required=True)
    comments = forms.CharField(required=False)
