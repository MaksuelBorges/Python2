from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def home(request):
    now = datetime.datetime.now()
    html = '<html><body> Agora é %s. </html></body>' % now
    return HttpResponse(html)