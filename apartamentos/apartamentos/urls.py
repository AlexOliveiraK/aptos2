from django.urls import path
from app_cad_usuarios import views as views_usuarios
from app_catalogo import views as views_catalogo

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views_catalogo.catalogo, name='catalogo-aptos'),
    path('novo_apto/', views_catalogo.novoApto, name='novo-apto'),
    path('salvar_apto/', views_catalogo.salvarApto, name='salvar-apto'),
    path('edita_apto/', views_catalogo.editaApto, name='edita-apto'),
    path('usuarios/', views_usuarios.usuarios, name='listagem-usuarios'),
    path('add_usuario/', views_usuarios.addUsuario, name='add-usuarios'),
    path('salvar_usuario/', views_usuarios.salvarUsuario, name='salvar-usuario'),
]

#+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)