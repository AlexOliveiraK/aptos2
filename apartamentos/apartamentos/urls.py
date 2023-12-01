from django.urls import path
from app_cad_usuarios import views as views_usuarios
from app_catalogo import views as views_catalogo

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views_catalogo.catalogo, name='catalogo_aptos'),
    path('usuarios/', views_usuarios.usuarios, name='listagem_usuarios'),
    path('add_usuario/', views_usuarios.add_usuario, name='add_usuarios'),
    path('novoapto/', views_catalogo.novoapto, name='novo_apto'),
    ]
    # path('', views.home, name='home'),
    # path('usuarios/', views.usuarios, name='listagem_usuarios'),
    # path('catalogo/', views_catalogo.catalogo, name='catalogo_aptos'),
    # path('novoapto/', views_catalogo.novoapto, name='novo_apto'),

#+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)