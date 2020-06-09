release: python manage.py migrate
web: gunicorn --pythonpath CarmelaSutra --env DJANGO_SETTINGS_MODULE=CarmelaSutra.settings CarmelaSutra.wsgi:application
