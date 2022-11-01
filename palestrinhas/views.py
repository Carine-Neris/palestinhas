from django.shortcuts import render

from .models import Palestras


def index(request):
    return render(request, 'palestras/index.html')