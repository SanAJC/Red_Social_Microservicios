#!/bin/sh
set -e

echo "Waiting for database..."
# Esperar a que la base de datos esté lista (podrías agregar un pequeño script de espera aquí)
sleep 5

echo "Running migrations..."
python manage.py migrate --noinput

echo "Starting service..."
exec "$@"