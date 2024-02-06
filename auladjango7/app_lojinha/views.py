from django.shortcuts import render
from models import Usuarios

# Create your views here.
def home(request):
    return render(request, 'home.html')

def usuarios(request):
    Novo_usuario = Usuarios()
    Novo_usuario.nome = request.POST.get('nome')
    Novo_usuario.idade = request.POST.get('idade')
    Novo_usuario.save()
    
    usuarios = {
        'usuarios':Usuarios.obeject.all()
    }
    return render(request, 'usuarios.html')


