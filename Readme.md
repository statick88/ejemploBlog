# My Blog

Este es un proyecto de ejemplo de un blog creado con Django.

## Requisitos

- Python 3.8 o superior
- Django 3.2 o superior

## Creación del proyecto

1. Instala Django si aún no lo has hecho. Puedes hacerlo con pip:

```bash
pip install django
```

2. Crea un nuevo proyecto de Django con el comando django-admin startproject. Por ejemplo:
```bash
django-admin startproject myblog
```
3. Navega al directorio del proyecto:
```bash
cd myblog
```
4. Crea una nueva aplicación dentro del proyecto:
```bash
python manage.py startapp blog
```

## Configuración del proyecto

1. Añade tu nueva aplicación a la lista INSTALLED_APPS en el archivo settings.py de tu proyecto.
```python
INSTALLED_APPS = [
    ...
    'blog',
]
```

2. Crea un modelo Post en el archivo models.py de tu aplicación. Un ejemplo de modelo Post se proporciona en este repositorio.

3. Después de crear tu modelo, crea una migración y aplícala a tu base de datos con los siguientes comandos:

```bash
python manage.py makemigrations blog
python manage.py migrate
```

4. Registra tu modelo Post en el archivo admin.py de tu aplicación para que aparezca en el panel de administración.

```python
from django.contrib import admin
from .models import Post

admin.site.register(Post)
```
5. Crea un superusuario para acceder al panel de administración:
```bash
python manage.py createsuperuser
```
6. Inicia tu servidor con python manage.py runserver y visita http://127.0.0.1:8000/admin/ en tu navegador. Deberías poder iniciar sesión con tu superusuario y crear posts a través de la interfaz de administración.

## Plantillas

Este proyecto utiliza el sistema de plantillas de Django. Hay una plantilla base (base.html) que define una estructura básica para las páginas del sitio. Otras plantillas, como post_list.html, extienden esta plantilla base e insertan su propio contenido.

## Formularios

Este proyecto utiliza el sistema de formularios de Django para la creación de posts. Hay un formulario PostForm que permite a los usuarios ingresar un título y texto para un post. Este formulario se utiliza en la vista post_new y su correspondiente plantilla.

## Más información

Para obtener más información sobre cómo trabajar con Django, consulta la documentación oficial de Django.
