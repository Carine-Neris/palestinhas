from django.shortcuts import render
from django.http import HttpResponse

from .models import Palestras
from .forms import PalestraForm


def palestras(request):
    if request.method == 'GET':
        palestras = Palestras.objects.all()
        form = PalestraForm()
        context = {'context': palestras,
                    'form': form}
        return render(request,'palestras/index.html',context)

    elif request.method == 'POST':
        palestras = Palestras.objects.all()
        form = PalestraForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
        form = PalestraForm()
        context = {'context': palestras,
                    'form': form}
        return render(request,'palestras/index.html', context)
  
        