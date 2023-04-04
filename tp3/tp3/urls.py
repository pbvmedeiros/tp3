"""tp3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('usuarios/', views.usuarios, name='usuarios'),
    path('productos/', views.productos, name='productos'),
    path('tiendas/', views.tiendas, name='tiendas'),
    path('crear_usuario/', views.crear_usuario, name='crear_usuario'),
    path('crear_producto/', views.crear_producto, name='crear_producto'),
    path('crear_tienda/', views.crear_tienda, name='crear_tienda'),
    path('buscar/', views.buscar, name='buscar'),
    path('admin/', admin.site.urls),
]
