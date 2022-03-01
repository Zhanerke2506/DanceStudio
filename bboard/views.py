from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
import datetime
from .models import Bb


def index(request) :
    return render(request, 'index.html')

def aboutus(request) :
    return render(request, 'about-us.html')

def choreo(request) :
    return render(request, 'choreographers.html')