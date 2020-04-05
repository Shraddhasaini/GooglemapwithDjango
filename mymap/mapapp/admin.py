# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
#from django_google_maps import widgets as map_widgets
#from django_google_maps import fields as map_fields
from .models import *
admin.site.register(Geolocation)
