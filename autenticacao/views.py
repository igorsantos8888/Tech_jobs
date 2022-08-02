from django.shortcuts import redirect, render
from django.http import HttpResponse
from autenticacao.models import UserJob
from .forms import UserJobForm
from django.contrib import messages
from django.contrib.messages import constants

def cadastro(request):
    if request.method == 'GET':
        
        usuarios = UserJob.objects.all()
        
        form = UserJobForm()
        
        context = {
            'usuarios': usuarios,
            'form': form,
        }
        
        return render(request, 'cadastro.html', context)
    elif request.method == 'POST':
        form = UserJobForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.add_message(request, constants.SUCCESS, 'Usuário cadastrado com sucesso')
            return redirect('cadastro')
        else:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
            usuarios = UserJob.objects.all()
        
            form = UserJobForm()
            
            context = {
                'usuarios': usuarios,
                'form': form,
            }
            return render(request, 'cadastro.html', context)