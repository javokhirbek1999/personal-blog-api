release: python manage.py collectstatic --noinput
release: python manage.py makemigrations --no-input
release: python manage.py migrate --no-input

web: gunicorn core.wsgi
