"""
URL configuration for ARPortfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.http import HttpResponse
import os

def robots_txt(request):
    robots_path = os.path.join(settings.STATIC_ROOT or settings.STATICFILES_DIRS[0], 'robots.txt')
    try:
        with open(robots_path, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        content = "User-agent: *\nAllow: /\nSitemap: https://donaldozoubery.com/sitemap.xml"
    return HttpResponse(content, content_type='text/plain')

def sitemap_xml(request):
    sitemap_path = os.path.join(settings.STATIC_ROOT or settings.STATICFILES_DIRS[0], 'sitemap.xml')
    try:
        with open(sitemap_path, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        content = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
        <loc>https://donaldozoubery.com/</loc>
        <lastmod>2025-01-02</lastmod>
        <changefreq>weekly</changefreq>
        <priority>1.0</priority>
    </url>
</urlset>"""
    return HttpResponse(content, content_type='application/xml')

urlpatterns = [
    # For Dev only
    path('admin/', admin.site.urls),
    path('', include("apps.portfolio.urls")),
    path('robots.txt', robots_txt),
    path('sitemap.xml', sitemap_xml),
]

handler404 = "apps.portfolio.views.handle_not_found"

# Configuration pour servir les fichiers statiques et média
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    # En production, WhiteNoise s'occupe des fichiers statiques
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
