from django.shortcuts import redirect, render
from django.http import HttpResponse
from autenticacao.models import UserJob
from .forms import UserJobForm

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
            return redirect('cadastro')
        else:
            usuarios = UserJob.objects.all()
        
            form = UserJobForm()
            
            context = {
                'usuarios': usuarios,
                'form': form,
            }
            return render(request, 'cadastro.html', context)