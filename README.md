# Django, DRF with Postgresql using Hyperlink Serializer Model of CURD operations in multiple model  

## Concepts of Athletics applications 

## Create Database

## Create and activate virtual environment

## Installed Packages or Dependencies 

````python pip install django, djangorestframework, psycopg2
````

## Create django project and app

````python 
django-admin startproject athlets_api

django-admin startapp athlets_app
````
## Application definition(settings.py)

````python 
INSTALLED_APPS = [
    'athlets_app',
    'rest_framework',
]
````
## DB Connections (settings.py)

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'DRONE',
        'USER': 'postgres',
        'PASSWORD': '********',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## Applications urls

````python API URLS - 
     
     http://127.0.0.1:8000/api/
    "athletics/category": "http://127.0.0.1:8000/api/athletics/category/",
    "athletics": "http://127.0.0.1:8000/api/athletics/",
    "players": "http://127.0.0.1:8000/api/players/",
    "competitions": "http://127.0.0.1:8000/api/competitions/"
````




