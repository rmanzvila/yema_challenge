# -*- coding: utf-8 -*-

import uuid
from django.db import models
from django.utils.translation import ugettext_lazy as _


class UUIDPrimaryKeyModelMixin(models.Model):
    """An abstract base class model that provides an uuid field that is the primary key."""

    uuid = models.UUIDField(
        verbose_name='UUID',
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    class Meta:
        abstract = True


class TimeStampedModelMixin(models.Model):
    """Timestamp extra field."""

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated at'))

    class Meta:
        abstract = True
        ordering = ['-created_at', '-updated_at']