# -*- coding: utf-8 -*-

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone


def send_email(subject, to, html_body):
    """Helps to send and email."""
    email = EmailMultiAlternatives(
        subject=subject,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=to
    )

    email.attach_alternative(html_body, 'text/html')
    email.send()


def generate_body(appointment):
    """Create html body for email."""
    appointment_time = timezone.localtime(appointment.appointment_time)
    date_time = appointment_time.strftime("%m/%d/%Y, %H:%M:%S")
    return '<strong>{0}</strong>' \
           '<br><br>' \
           '*{1} : {2} {3}<br>'\
           '*{4} : {5} {6}<br>'\
           '*{7} : {8}<br>'\
           '*{9} : {10}<br>'\
        .format(
            _('Detail appointment'),
            _('Patient name'),
            appointment.patient.name,
            appointment.patient.last_name,
            _('Doctor name'),
            appointment.doctor.name,
            appointment.doctor.last_name,
            _('Appointment date'),
            date_time,
            _('Comments'),
            appointment.comments
        )
