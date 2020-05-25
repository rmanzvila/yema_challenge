# -*- encoding:utf-8 -*-

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.redirects.models import Redirect
from django.urls import path
from django.views.generic import TemplateView
from django.contrib.sites.models import Site
from rest_framework.authtoken.models import Token

admin.site.site_header = 'Yema Test - Ricardo Manzanares Avila'
admin.site.site_title = 'Yema Test - Ricardo Manzanares Avila'
admin.site.index_title = 'Yema Test - Ricardo Manzanares Avila'

admin.site.unregister(Site)
admin.site.unregister(Redirect)
admin.site.unregister(Token)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
