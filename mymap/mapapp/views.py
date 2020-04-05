# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.template import loader

#
def index(request):
    latitude=request.GET.get('latitude', 0)
    longitude =request.GET.get('longitude', 0)
    template = loader.get_template('mapapp/index.html')
    context = {
        'latitude': latitude, 'longitude': longitude,
    }
    return HttpResponse(template.render(context, request))

#
