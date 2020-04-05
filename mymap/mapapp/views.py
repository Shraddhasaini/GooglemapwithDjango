# -*- coding: utf-8 -*-
#from __future__ import unicode_literals
from django.http import HttpResponse
from django.template import loader

from .models import Rental


def index(request):
    template = loader.get_template('mapapp/index.html')
    context = {
        'latitude': -0.344, 'longitude': 11.036,
    }
    return HttpResponse(template.render(context, request))
