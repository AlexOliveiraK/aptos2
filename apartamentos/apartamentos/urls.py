from django.urls import path
from app_cad_usuarios import views
from app_catalogo import views as views_catalogo
from django.conf import settings
from django.conf.urls.static import static
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
print(os.path.join(BASE_DIR, 'static'))

#  os.path.join(BASE_DIR, 'static')
# print("ECA")
# print(static("/static/", document_root=f"{os.path.join(BASE_DIR, 'static')}"))
#print(static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
#print(settings.STATIC_ROOT)
urlpatterns = [
    path('', views.home, name='home'),
    path('usuarios/', views.usuarios, name='listagem_usuarios'),
    path('catalogo/', views_catalogo.catalogo, name='catalogo_aptos'),
    path('novoapto/', views_catalogo.novoapto, name='novo_apto'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)