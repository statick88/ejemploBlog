from django.urls import path
from . import views  # Importa las vistas de la aplicación blog

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    # Agrega aquí más rutas según sea necesario
]