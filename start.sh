#!/bin/bash

echo Starting Gunicorn.
exec python3 manage.py runserver -h 0.0.0.0 -p 8000
#exec gunicorn manage:manager \
#    --bind 0.0.0.0:8000 \
#    --workers 3