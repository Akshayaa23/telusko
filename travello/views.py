from django.shortcuts import render
from .models import Destintion

import json
# Create your views here.

def index(request):
    
    dests = Destination.objects.all()

    return render(request, 'index.html',{'dests' : dests})
