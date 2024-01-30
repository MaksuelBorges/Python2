from django.shortcuts import render
from datetime import datetime
from random import randint

# Create your views here.
def home(request):
    dados = {
        'nomes': ['Maksuel', 'Moraes', 'Halland'],
        'horario': datetime.now().strftime('%H:%M:%S'),
        'numero': randint(0, 100)
    }
    return render(request, 'index.html', dados)