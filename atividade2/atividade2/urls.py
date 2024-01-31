from django.contrib import admin
from django.urls import path
from blog import views
from django.http import HttpResponse

urlpatterns = [
    path('', views.home),
]
