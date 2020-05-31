release: python CarmelaSutra/manage.py makemigrations
release: python CarmelaSutra/manage.py migrate
web: gunicorn --pythonpath CarmelaSutra --env DJANGO_SETTINGS_MODULE=CarmelaSutra.settings CarmelaSutra.wsgi:application
