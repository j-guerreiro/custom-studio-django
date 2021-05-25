#from django.forms import ModelForm
from django.shortcuts import render, redirect
from .models import Equipamento

# view da home
def index(request):
    return render(request, 'app/index.html', {})


#view da listagem de equipamentos
def equipamento_list(request):
    equipamentos = Equipamento.objects.all()
    return render(request, '/equipamento_list.html', { 'equipamentos': equipamento})