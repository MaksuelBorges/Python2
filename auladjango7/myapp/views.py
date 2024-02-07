from django.shortcuts import render

# Create your views here.

def home_page(request):
    return render(request, "home.html")
def forumlario_page(request):
    return render(request, "formulario.html")