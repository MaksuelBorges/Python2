from django.shortcuts import render

# Create your views here.
def conta(request):
    return render(request,'index.html')