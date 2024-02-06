from django.contrib import admin
from django.urls import path
from app_lojinha import views
from .views import ListUsuariosView

urlpatterns = [
    path('', views.home),
    path('usuarios', ListUsuariosView.as_view(), name='list_usuarios')
]
