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
def diretion(request):
    destination=request.GET.get('destination', 0)
    origin =request.GET.get('origin', 0)
    template = loader.get_template('mapapp/diretion.html')
    context = {
        'destination': destination, 'origin': origin,
    }
    return HttpResponse(template.render(context, request))
