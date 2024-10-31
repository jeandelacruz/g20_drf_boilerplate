# DRF Boilerplate

## Instalación

```sh
pip install install Django
```

## Iniciar Django

- Crear un proyecto

```sh
django-admin startproject <nombre_proyecto> .
```

- Iniciar proyecto

```sh
python manage.py runserver
```

- Crear superusuario (Se ejecuta despues de las migraciones)

```sh
python manage.py createsuperuser
```

## Apps

1. Modularidad
2. Reutilización
3. Desacoplamiento
4. Escalabilidad
5. Enfoque en la funcionalidad

- Crear una app

```sh
python manage.py startapp <nombre_app>
```

## Migraciones

- Sincronizar o Aplicar migraciones

```sh
python manage.py migrate
```

- Crear una migración

```sh
python manage.py makemigrations
python manage.py makemigrations <nombre_app>
```

## Variables de Entorno

```sh
DEBUG=True

DB_NAME=''
DB_USER='postgres'
DB_PASSWORD=''
DB_HOST='127.0.0.1'
DB_PORT='5432'
```