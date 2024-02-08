from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin', admin.site.urls),
    path('', views.home_page),
    path('cadastro', views.cadastro_page),
    path('consulta', views.consulta_page)
]
