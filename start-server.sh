#! /usr/bin/env bash
# start-server.sh

if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ]; then
  (cd study; python manage.py createsuperuser --no-input)
fi
(cd study; uwsgi --ini config/uwsgi_docker.ini) &
nginx -g "daemon off;"