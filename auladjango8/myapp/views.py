from django.shortcuts import render
from .models import Pessoa
from django.http import HttpResponseRedirect, HttpResponseBadRequest

# Create your views here.
def cadastro_page(request):
    return render(request, 'cadastro.html')

def consulta_page(request):
    if request.method == 'GET':
        return render(request, 'consulta.html')
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        pais = request.POST.get('pais')
        estado = request.POST.get('estado')
        cidade = request.POST.get('cidade')
        pessoa = Pessoa()
        pessoa.nome = nome
        pessoa.pais = pais
        pessoa.estado = estado
        pessoa.cidade = cidade
        pessoa.save()
        return HttpResponseRedirect('consulta.html')
    else:
        return HttpResponseBadRequest()
        

def home_page(request):
    return render(request, 'home.html')