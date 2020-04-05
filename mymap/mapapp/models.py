# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django_google_maps import fields as map_fields

class Geolocation(models.Model):
    longitude = models.FloatField("Longitude", default=0)
    latitude = models.FloatField("Latitude", default=0)
