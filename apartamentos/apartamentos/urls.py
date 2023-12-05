from django.urls import path
from app_cad_usuarios import views as views_usuarios
from app_catalogo import views as views_catalogo

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views_catalogo.catalogo, name='catalogo_aptos'),
    path('novoapto/', views_catalogo.novoapto, name='novo_apto'),
    path('salvar-apto/', views_catalogo.salvarApto, name='salvar_Apto'),
    path('usuarios/', views_usuarios.usuarios, name='listagem_usuarios'),
    path('add_usuario/', views_usuarios.add_usuario, name='add_usuarios'),
    path('salvar_usuario/', views_usuarios.salvarUsuario, name='salvar_usuario'),
]

#+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)