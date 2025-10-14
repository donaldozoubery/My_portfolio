# Procfile pour le déploiement sur Heroku/Render
web: gunicorn config.wsgi:application --log-file -
release: python manage.py migrate
