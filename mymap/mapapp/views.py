# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.template import loader
from .models import *
#
def index(request):
    latitude=request.GET.get('latitude', 0)
    longitude =request.GET.get('longitude', 0)
    Geolocation.objects.create(latitude=latitude,longitude=longitude)
    history= Geolocation.objects.all()
    template = loader.get_template('mapapp/index.html')
    context = {
        'latitude': latitude, 'longitude': longitude,'history':history
    }
    print(latitude,longitude)
    return HttpResponse(template.render(context, request))

#
