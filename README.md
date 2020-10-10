## How to setup project locally?

#### 1. Create virtualenv inside main project directory, and activate it

``` shell script
python3 -m venv venv
source venv/bin/activate
```

#### Install all dependencies

``` shell script
pip install -r requirements.txt
```

## Add Database Settings
1. Create local_settings.py file
``` shell script
touch ecommerce_api/local_settings.py
```

2. Add your database setting in it. (Change values according to your db setup)
``` python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'PORT': '5432',
        'HOST': 'localhost',
        'USER': 'postgres',
        'PASSWORD': 'password'
    }
}
```

#### Run Django server

``` shell script
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
