# -*- encoding:utf-8 -*-
from django import forms
from rest_framework.exceptions import ValidationError

from apps.appointment.models import Doctor, Patient
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


def found_doctor(value):
    try:
        Doctor.objects.get(uuid=value)
    except Doctor.DoesNotExist:
        raise ValidationError(_('Object not found'))
    return value


def found_patient(value):
    try:
        Patient.objects.get(uuid=value)
    except Patient.DoesNotExist:
        raise ValidationError(_('Object not found'))
    return value


class AppointmentForm(forms.Form):
    doctor = forms.CharField(required=True, validators=[found_doctor])
    patient = forms.CharField(required=True, validators=[found_patient])
    appointment_time = forms.DateTimeField(required=True)
    comments = forms.CharField(required=False)


class AppointmentCompleteForm(forms.Form):
    doctor = forms.CharField(required=True, validators=[found_doctor])
    name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    age = forms.IntegerField(required=False)
    appointment_time = forms.DateTimeField(required=True)
    comments = forms.CharField(required=False)


