from django.shortcuts import render, redirect,get_object_or_404

from .models import Palestras, Comentarios
from .forms import PalestraForm, ComentariosForm


def palestras(request):
    palestras = Palestras.objects.all().order_by('-data_criacao')
    form = PalestraForm()
    context = {'context': palestras, 'form': form}
    return render(request, 'palestras/index.html', context)


def palestras_by_user(request):
    palestras = Palestras.objects.filter(user=request.user.id)
    form = PalestraForm()
    context = {'context': palestras, 'form': form}
    return render(request,'palestras/palestras_by_user.html', context)


def palestra_create(request):
    if request.method == 'POST':
        form = PalestraForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
    return redirect('palestras')


def palestra_delete(request, pk):
    palestra = Palestras.objects.get(pk=pk)
    palestra.delete()
    return redirect('palestras')


def palestra_detail(request, pk):
    if request.method == 'GET':
        palestra = Palestras.objects.get(pk=pk)
        comentarios = Comentarios.objects.filter(palestra=pk)

        context = {'palestra': palestra, 'comentarios':comentarios}
        return render(request, 'palestras/palestra_detail.html', context)


def palestra_edit(request,pk):
    if request.method == 'POST':
        palestra = Palestras.objects.get(pk=pk)
        form = PalestraForm(request.POST, instance=palestra)
        if form.is_valid():
            form.save()
            return redirect('palestras')
        else:
            context = {'palestra': palestra,
                       'form': form}
            return render(request, 'palestras/palestra_edit.html', context)


def adicionar_comentario(request, palestra_id):
    palestra = get_object_or_404(Palestras, id=palestra_id)
    if request.method == "POST":
        form_comment = ComentariosForm(request.POST)
        if form_comment.is_valid():
            comentario = form_comment.save(commit=False)
            comentario.user = request.user
            comentario.palestra = palestra
            comentario.save()
        return redirect('palestradetail', pk=palestra.pk)
    