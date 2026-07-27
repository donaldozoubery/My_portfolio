import os
from pathlib import Path
from django.core.wsgi import get_wsgi_application
from django.conf import settings
from django.http import FileResponse

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
application = get_wsgi_application()

STATIC_DIR = Path(settings.BASE_DIR) / 'static'
MEDIA_DIR = Path(settings.BASE_DIR) / 'media'


FAVICON_PATHS = [
    Path(settings.BASE_DIR) / 'static' / 'assets' / 'img' / 'favicon.ico',
    STATIC_DIR / 'favicon.ico',
    Path(settings.BASE_DIR) / 'favicon.ico',
]


class StaticFileMiddleware:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        path_info = environ.get('PATH_INFO', '')

        if path_info.startswith('/static/'):
            file_path = STATIC_DIR / path_info[len('/static/'):]
            if file_path.exists() and file_path.is_file():
                return FileResponse(open(file_path, 'rb'))(environ, start_response)

        if path_info.startswith('/media/'):
            file_path = MEDIA_DIR / path_info[len('/media/'):]
            if file_path.exists() and file_path.is_file():
                return FileResponse(open(file_path, 'rb'))(environ, start_response)

        if path_info == '/favicon.ico':
            for favicon_path in FAVICON_PATHS:
                if favicon_path.exists() and favicon_path.is_file():
                    return FileResponse(open(favicon_path, 'rb'))(environ, start_response)

        return self.app(environ, start_response)


application = StaticFileMiddleware(application)
