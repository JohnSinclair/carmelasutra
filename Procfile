release: python CarmelaSutra/manage.py migrate
release: python CarmelaSutra/manage.py makemigrations
web: gunicorn --env DJANGO_SETTINGS_MODULE=CarmelaSutra.CarmelaSutra.settings CarmelaSutra.CarmelaSutra.wsgi:application
