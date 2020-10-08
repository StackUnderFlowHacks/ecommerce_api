## How to setup project locally?

#### 1. Create virtualenv inside main project directory, and activate it

``` shell script
python3 -m venv env
source env/bin/activate
```

#### Install all dependencies

``` shell script
pip install -r requirements.txt
```

#### Run Django server

``` shell script
python manage.py migrate
python manage.py runserver
```

Test Edit
