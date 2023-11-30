from django.urls import path
from app_cad_usuarios import views
from app_catalogo import views as views_catalogo
from django.conf import settings
from django.conf.urls.static import static
import os
from pathlib import Path
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path(
        "admin/",
        include(
            [
                path("", admin.site.urls),
            ]
        ),
    ),    
    path('', views.home, name='home'),
    path('usuarios/', views.usuarios, name='listagem_usuarios'),
    path('catalogo/', views_catalogo.catalogo, name='catalogo_aptos'),
    path('novoapto/', views_catalogo.novoapto, name='novo_apto'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)