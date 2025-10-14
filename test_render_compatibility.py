#!/usr/bin/env python
"""
Script pour tester la compatibilité avec Render
"""
import os
import sys

print("=== TEST COMPATIBILITE RENDER ===")

# Test des versions Python
print(f"Python version: {sys.version}")

# Test des dépendances critiques
try:
    import django
    print(f"Django version: {django.get_version()}")
except ImportError:
    print("ERREUR: Django non installé")

try:
    from PIL import Image
    print(f"Pillow version: {Image.__version__}")
except ImportError:
    print("ERREUR: Pillow non installé")

try:
    import psycopg2
    print(f"psycopg2 version: {psycopg2.__version__}")
except ImportError:
    print("ERREUR: psycopg2 non installé")

try:
    import cloudinary
    print("Cloudinary: OK")
except ImportError:
    print("ERREUR: Cloudinary non installé")

try:
    import xhtml2pdf
    print("xhtml2pdf: OK")
except ImportError:
    print("ERREUR: xhtml2pdf non installé")

# Test des variables d'environnement
print("\n=== VARIABLES ENVIRONNEMENT ===")
env_vars = [
    'DEBUG', 'SECRET_KEY', 'DATABASE_URL', 'ALLOWED_HOSTS',
    'CLOUD_NAME', 'CLOUD_API_KEY', 'CLOUD_API_SECRET'
]

for var in env_vars:
    value = os.environ.get(var, 'NON DEFINIE')
    if var in ['SECRET_KEY', 'CLOUD_API_KEY', 'CLOUD_API_SECRET']:
        value = '***' if value != 'NON DEFINIE' else 'NON DEFINIE'
    print(f"{var}: {value}")

print("\n=== RECOMMANDATIONS RENDER ===")
print("1. Utiliser Python 3.11.0 (pas 3.13)")
print("2. Pillow >= 10.4.0 pour compatibilité")
print("3. Variables d'environnement configurées")
print("4. Base de données PostgreSQL")
print("5. Fichiers statiques collectés")

print("\n=== COMMANDES DEPLOIEMENT ===")
print("1. git add .")
print("2. git commit -m 'Fix Render deployment'")
print("3. git push origin main")
print("4. Vérifier les logs sur Render")
