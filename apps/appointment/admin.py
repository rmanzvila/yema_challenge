# -*- coding: utf-8 -*-

from django.contrib import admin
from apps.appointment.models import Doctor, Patient, Appointment
from django.utils.translation import ugettext_lazy as _
from django.contrib import messages
from apps.contrib.utils.email import send_email, generate_body


@admin.register(Doctor)
class DoctorAdmin( admin.ModelAdmin):
    """Defines the doctor admin."""

    list_display = [
        'uuid',
        'name',
        'last_name',
        'email',
        'created_at',
        'updated_at'
    ]
    search_fields = ('uuid', 'name', 'last_name', 'email')


@admin.register(Patient)
class PatientAdmin( admin.ModelAdmin):
    """Defines the Patient admin."""

    list_display = [
        'uuid',
        'name',
        'last_name',
        'email',
        'created_at',
        'updated_at'
    ]
    search_fields = ('uuid', 'name', 'last_name', 'email')


@admin.register(Appointment)
class AppointmentAdmin( admin.ModelAdmin):
    """Defines the appointment admin."""

    list_display = [
        'uuid',
        'appointment_time',
        'get_doctor_name',
        'get_patient_name',
        'created_at',
        'updated_at'
    ]
    search_fields = ('doctor__name', 'doctor__last_name', 'doctor__email', 'patient__name', 'patient__last_name',)
    list_filter = ('appointment_time',)
    raw_id_fields = ['doctor', 'patient']

    def get_doctor_name(self, obj):
        return '{0} {1}'.format(
            obj.doctor.name,
            obj.doctor.last_name
        )

    def get_patient_name(self, obj):
        return '{0} {1}'.format(
            obj.patient.name,
            obj.patient.last_name
        )

    get_doctor_name.admin_order_field = _('Doctor name')
    get_doctor_name.short_description = _('Doctor name')
    get_patient_name.admin_order_field = _('Patient name')
    get_patient_name.short_description = _('Patient name')

    def send_by_email(self, request, queryset):
        counter = 0
        for appointment in queryset:
            email_to = appointment.patient.email
            if email_to:
                html_content = generate_body(appointment)
                send_email(_('Appointment detail'), [email_to], html_content)
                counter += 1

        messages.info(request, _('Emails sent: ') + str(counter))

    send_by_email.short_description = _('Send by email to patient')
    actions = ['send_by_email', ]

