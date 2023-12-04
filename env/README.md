# Proyecto DevBlog

## Descripción
Proyecto de blog para desarrolladores, donde se pueden crear, editar y eliminar posts, además de poder comentarlos.

## Instalación

* 1- Crear un entorno virtual con `python -m venv ./env/env1`
* 2- Activar el entorno virtual con `./env/env1/Scripts/activate`
* 3- Crear proyecto con `django-admin startproject dev_blog`
* 4- Acceder a la carpeta del proyecto con `cd dev_blog`
* 5- Iniciar el servidor con `python manage.py runserver`
* 6- Hacer overide de usuarios
    - 6.1- Crear aplicación con `python manage.py startapp users`
    - 6.2- añadir users a settings.py del proyecto
    - 6.3- Configurar users admin.py
    - 6.4- Configurar users  models.py
    - 6.5- Indicar a Django que use nuestro modelo personalizado en settings.py
    - 6.6- Crear migraciones con `python manage.py makemigrations`
    - 6.7- Aplicar migraciones con `python manage.py migrate`
    - 6.8- Crear superusuario con `python manage.py createsuperuser`
    - 6.9- Modificar el modelo user para iniciar sesión con el email
* 7- Instalar Django Rest Framework con `pip install djangorestframework`
* 8- Crear aplicación posts con `python manage.py startapp posts`
    - 8.1- Agregar rest_framework a settings.py
    - 8.2- [Documentacion](https://www.django-rest-framework.org/)
* 9- Instalar libreria de la documentacion "def-yasg" con `pip install -U drf-yasg`
    - 9.1- Agregar rest_framework_swagger a settings.py
    - 9.2- instalar libreria `pip install -U setuptools`
    - 9.3- [Documentacion](https://drf-yasg.readthedocs.io/en/stable/readme.html#installation)
    - 9.4- Actualizar urls.py del proyecto
* 10- Generar archivos estáticos, primero se modifican los settings.py
    - 10.1- agregar debajo de STATIC_URL = 'static/' esta linea STATIC_ROOT = './static/'
    - 10.2- comando generar archivos estáticos: python manage.py collectstatic
* 11- Administracion de usuarios, configuraciones en la app users
    - 11.1- crear carpeta api
    - 11.2- crear archivo __init__.py, este archivo es para que python reconozca la carpeta como un paquete
    - 11.3- crear archivo serializers.py
    - 11.4- crear archivo views.py
    - 11.5- crear archivo router.py
    - 11.6- configurar archivos nuevos
    - 11.7- configurar urls.py del proyecto
    - 11.8- encrytar contraseñas, modificando el serializer.py
* 12 - Agregar autenticación por token, libreria simple JWT
    - [Documentacion](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html)
    - comando instalacion: `pip install djangorestframework-simplejwt`
    - configurar settings.py
    - configurar router.py de la app users
    - definir expiration del token en settings.py
    - verificar el token y expiracion en la consola de la app [jwt.io](https://jwt.io/)
    - agregar token y refresh en urls.py del proyecto
* 13 - Crear endpoint para obtener el usuario autenticado
    - crear archivo views.py en la app users
    - crear archivo urls.py en la app users
    - configurar urls.py del proyecto
* 14 - crear nueva app category
    - crear app con `python manage.py startapp category`
    - agregar app a settings.py
    - crear modelo en models.py de la app category
    - crear migraciones con `python manage.py makemigrations`
    - aplicar migraciones con `python manage.py migrate`
    - agregar modelo al admin.py de la app category
    - crear carpeta api
    - crear archivo __init__.py dentro de la carpeta api
    - crear archivo serializers.py dentro de la carpeta api
    - crear archivo views.py dentro de la carpeta api
    - crear archivo router.py dentro de la carpeta api
    - configurar archivos
    - configurar urls.py del proyecto
    - crear migraciones con `python manage.py makemigrations`
    - aplicar migraciones con `python manage.py migrate`
    - agregar permisos a los endpoints, de escritura
    - crear en la app category un archivo permissions.py dentro de la carpeta api
    - configurar archivo permissions.py
    - configurar archivo views.py
* 15 - instalar libreria django-filter
    - [Documentacion](https://django-filter.readthedocs.io/en/stable/guide/rest_framework.html)
    - instalar libreria con `pip install django-filter`
    - agregar django_filters a settings.py
    - configurar archivo views.py de la app category
* 16 - crear aplicacion posts
    - crear app con `python manage.py startapp posts`
    - agregar app a settings.py
    - crear modelo en models.py de la app posts
    - crear migraciones con `python manage.py makemigrations`
    - aplicar migraciones con `python manage.py migrate`
    - agregar modelo al admin.py de la app posts
* 17 - manejo de imagenes 
    - instalar libreria Pillow con `pip install Pillow`
    - crear carpeta media en la raiz del proyecto
* 18 - agregar operciones del crud
    - crear carpeta api
    - crear archivo __init__.py dentro de la carpeta api
    - crear archivo serializers.py dentro de la carpeta api
    - crear archivo views.py dentro de la carpeta api
    - crear archivo router.py dentro de la carpeta api
    - configurar archivos
    - configurar urls.py del proyecto
    - crear migraciones con `python manage.py makemigrations`
    - aplicar migraciones con `python manage.py migrate`
    - agregar permisos a los endpoints, de escritura
    - crear en la app posts un archivo permissions.py dentro de la carpeta api
    - configurar archivo permissions.py
    - configurar archivo views.py
* 19 - crear aplicaciones de comentarios
    - crear app con `python manage.py startapp comments`
    - agregar app a settings.py
    - crear modelo en models.py de la app comments
    - crear migraciones con `python manage.py makemigrations`
    - aplicar migraciones con `python manage.py migrate`
    - agregar modelo al admin.py de la app comments
    - crear carpeta api
    - crear archivo __init__.py dentro de la carpeta api
    - crear archivo serializers.py dentro de la carpeta api
    - crear archivo views.py dentro de la carpeta api
    - crear archivo router.py dentro de la carpeta api
    - configurar archivos
    - configurar urls.py del proyecto
* 20 - despluegue
    - ejecutar comando ```pip freeze > requirements.txt```, genera un archivo con las dependencias
    - desactivar el debug, en settings.py del proyecto
    - agregar el host, en settings.py del proyecto
    - crear archivo runtime.txt, configurar archivo
    - crear archivo procfile.txt, configurar archivo
    - instalar libreria gunicorn: ```pip install gunicorn```
    - agregar la libreria a requirements.txt, ejecutando de nuevo el comando
    - borrar migraciones de las aplicaciones y base de datos

# Hosting en https://www.pythonanywhere.com/
* 1- registrarse
* 2- confirmar correo
* 3- elegir una version de python
* 4- crear repositorio
* 5- abrir consola, Bash console
* 6- clonar repositorio, git clone <https del repositorio>
* 7- crear maquina virtual: ```mkvirtualenv --python=/usr/bin/python3.7 venv```, la version de python depende de la elegida
* 8- debe tener el repositorio el archivo requirements.txt
* 9- ejecutar requirements.txt: ```pip install -r requirements.txt```



