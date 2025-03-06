from django.urls import path
from . import views
from .views import buscar, login, logout, perfil
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:receita_id>', views.receita, name='receita'),
    path('buscar/', views.buscar, name='buscar'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('perfil/', views.perfil, name='perfil'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)