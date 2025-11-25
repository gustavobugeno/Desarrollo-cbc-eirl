"""
URL configuration for cbc project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from core import views
from django.conf import settings
from django.conf.urls.static import static

from core.views_admin import create_admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('servicios/', views.servicios, name='servicios'),  
    path('contacto/', views.contacto, name='contacto'),
    path('solicitar-info/<int:servicio_id>/', views.solicitar_info, name='solicitar_info'),  
    path('gracias/', views.gracias, name='gracias'),

    # ⭐ Ruta para mostrar seguimiento por código
    path("seguimiento/<str:codigo>/", views.seguimiento, name="seguimiento"),

    # ⭐ Ruta para recibir el código desde el formulario GET y redirigir
    path("seguimiento/", views.seguimiento_base, name="seguimiento_base"),
    path('seguimiento/<str:codigo>/aprobar/', views.aprobar_solicitud, name='aprobar_solicitud'),
    path('seguimiento/<str:codigo>/rechazar/', views.rechazar_solicitud, name='rechazar_solicitud'),
    path('seguimiento/<str:codigo>/cambios/', views.solicitar_cambios, name='solicitar_cambios'),
    path("create-admin/", create_admin, name="create_admin"),

]


