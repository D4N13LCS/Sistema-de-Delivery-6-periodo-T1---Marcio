#!/bin/sh

python manage.py migrate

python seed.py || true

python manage.py runserver 0.0.0.0:$PORT