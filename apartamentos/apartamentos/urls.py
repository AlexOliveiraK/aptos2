from django.urls import path
from app_cad_usuarios import views as views_usuarios
from app_catalogo import views as views_catalogo
from app_dashboard import views as views_dashboard

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views_catalogo.catalogo, name='catalogo-aptos'),
    path('novo_apto/', views_catalogo.novoApto, name='novo-apto'),
    path('salva_novo_apto/', views_catalogo.salvaNovoApto, name='salva-novo-apto'),
    path('update_apto/', views_catalogo.updateApto, name='update-apto'),
    path('edita_apto/', views_catalogo.editaApto, name='edita-apto'),
    path('login/', views_usuarios.userLogin, name='user-login'),
    path('register/', views_usuarios.userRegister, name='user-register'),
    path('usuarios/', views_usuarios.usuarios, name='listagem-usuarios'),
    path('add_usuario/', views_usuarios.addUsuario, name='add-usuarios'),
    path('salvar_usuario/', views_usuarios.salvarUsuario, name='salvar-usuario'),
    path('dashboard/', views_dashboard.dashboard, name='abre-dashboard'),
]

#+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)