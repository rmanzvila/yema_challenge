# -*- coding: utf-8 -*-
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class AppointmentConfig(AppConfig):
    """Configuration for appointment process."""

    name = 'apps.appointment'
    verbose_name = _('Medical appointment')
    verbose_name_plural = _('Medical appointments'),
