# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Rental


def index(request):
    context = {latitude: -20.344, longitude: 131.036}
    return render(request, 'mapapp/index.html', context)
