# -*- coding: utf-8 -*-

from django.urls import include, path

app_name = 'appointment'
urlpatterns = [
    path('v1/', include('apps.appointment.api.v1.urls', namespace='v1')),
]
