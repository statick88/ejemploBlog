from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),  # Esto incluirá las urls de la aplicación blog en la ruta raíz
]