# -*- coding: utf-8 -*-

from django.db import models
from apps.contrib.utils.mixins import UUIDPrimaryKeyModelMixin, TimeStampedModelMixin
from django.utils.translation import ugettext_lazy as _


class Doctor(UUIDPrimaryKeyModelMixin, TimeStampedModelMixin):
    """Represents the doctor info."""

    name = models.CharField(verbose_name=_('Name'), max_length=250)
    last_name = models.CharField(verbose_name=_('Last name'), max_length=250)
    email = models.EmailField(
        _('Email Address'),
        error_messages={
            'unique': _('A user with that email already exists.'),
        },
        unique=True,
        db_index=True,
    )

    def __str__(self):
        return '{0} {1} {2}'.format(self.name, self.last_name, self.email)

    class Meta:
        db_table = 'doctor'
        verbose_name = _('Doctor')
        verbose_name_plural = _('Doctors')
        app_label = 'appointment'


class Patient(UUIDPrimaryKeyModelMixin, TimeStampedModelMixin):
    """Represents patient info."""

    name = models.CharField(verbose_name=_('Name'), max_length=250)
    last_name = models.CharField(verbose_name=_('Last name'), max_length=250)
    email = models.EmailField(
        _('Email Address'),
        error_messages={
            'unique': _('A user with that email already exists.'),
        },
        blank=True
    )

    def __str__(self):
        return '{0} {1} {2}'.format(self.name, self.last_name, self.email)

    class Meta:
        db_table = 'patient'
        verbose_name = _('Patient')
        verbose_name_plural = _('Patient')
        app_label = 'appointment'


class Appointment(UUIDPrimaryKeyModelMixin, TimeStampedModelMixin):
    """Represents the appointment info."""

    doctor = models.ForeignKey('appointment.Doctor', verbose_name=_('Assigned to'), on_delete=models.PROTECT,
                               related_name='doctor_appointment'
                               )

    patient = models.ForeignKey('appointment.Patient', verbose_name=_('Requested by'), on_delete=models.PROTECT,
                                related_name='patient_appointment'
                                )

    appointment_time = models.DateTimeField(verbose_name=_('Appointment time'), blank=False )

    comments = models.TextField(verbose_name=_('Comments'))

    def __str__(self):
        return '{0} {1} - {2}'.format(self.patient.name, self.patient.last_name, self.doctor.email)

    class Meta:
        db_table = 'appointment'
        verbose_name = _('Appointment')
        verbose_name_plural = _('Appointment')
        app_label = 'appointment'
        ordering = ['-created_at']
