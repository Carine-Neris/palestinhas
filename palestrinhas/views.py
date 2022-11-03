from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Palestras
from .forms import PalestraForm


def palestras(request):
    palestras = Palestras.objects.all()
    form = PalestraForm()
    context = {'context': palestras,
                'form': form}
    return render(request,'palestras/index.html',context)


def palestra_create(request):
    if request.method == 'POST':
        form = PalestraForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
    return redirect('palestras')


def palestra_delete(request,pk):
    palestra =  Palestras.objects.get(pk=pk)
    palestra.delete()
    return redirect('palestras')
  
        