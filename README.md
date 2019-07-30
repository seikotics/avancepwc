# Fist stage - Scalable Web Platform / Primer avance - Plataforma Web (SWP)
django - bootstrapt.

A Web platform. framework for scalable projects,

## Features

- For Django 2.2 and Python 3.7
- Modern virtual environments with [pipenv](https://github.com/pypa/pipenv)
- Styling with [Bootstrap](https://github.com/twbs/bootstrap) v4.1.3

## First-time setup

1.  Make sure Python 3.7x and Pipenv are already installed. 
2.  Clone the repo and configure the virtual environment:

`` ``
```
$ git clone https://github.com/seikotics/avancepwc
$ cd django
$ pipenv install
$ pipenv shell
```

3.  Set up the initial migration.

```
(django) $ python manage.py makemigrations
(django) $ python manage.py migrate
```

4.  Create a superuser:

```
(django) $ python manage.py createsuperuser
```

5.  Confirm and run the project:

```
(django) $ python manage.py runserver
```

Load the platform at [http://127.0.0.1:8000]

