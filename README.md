# Django rest framework with docker and postgreSQL token authorization


# !!! postgres not working !!!
> terminal command
- work in repo
**folder/file**

## setup
> $ mkdir drf-auth

Use poetry to initialize folder 

> $ cd `drf-auth` 
> $ poetry init -n 
> $ poetry add django djangorestframework 
> $ poetry add --dev black 
> $ poetry shell 

> $ django-admin startproject tank_project .
> $ python manage.py startapp fish

# ! CHECKLIST ! 
**pyproject.toml**
```[tool.poetry.dependencies]
python = "~3.8"
django = "^3.0.7"
djangorestframework = "^3.11.0"
whitenoise = "^5.1.0"
django-cors-headers = "^3.4.0"
djangorestframework-simplejwt = "^4.4.0"
psycopg2-binary = "^2.8.5"
django-environ = "^0.4.5"
gunicorn = "^20.0.4"
```

> $ python manage.py collectstatic 
    - empty static/ and will create staticfiles/

> $ poetry export -f requirements.txt -o requirements.txt

**Dockerfile**
```FROM python:3.8-slim``` slim!!

**docker-compose.yml**
build with ```python /code/manage.py runserver 0.0.0.0:8000```
then switch to ```gunicorn project_name.wsgi:application --bind 0.0.0.0:8000```

**garden_project/.env**
- .env must be in project folder
```DEBUG=off```

**garden_project/settings.py**
- import environ
    - set casting, default value
- read env
    - secret key
    - debug
    - allowed hosts
- installed apps
- middleware
- databases
- static files
- rest framework
- cors origin whitelist

**garden_project/urls.py**
```from rest_framework_simplejwt import views as jwt_views```
```path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
```

