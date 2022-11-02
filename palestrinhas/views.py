from django.shortcuts import render
from django.http import HttpResponse

from .models import Palestras

def palestras_list(request):
    palestras = Palestras.objects.all()
    context = {'context':palestras}

    return render(request,'palestras/index.html',context)
  