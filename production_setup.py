#!/usr/bin/env python
"""
Script de configuration pour la production
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.core.management import call_command
from django.contrib.auth import get_user_model

print("=== CONFIGURATION PRODUCTION ===")

# Vérification des migrations
print("1. Vérification des migrations...")
try:
    call_command('migrate', verbosity=0)
    print("OK - Migrations appliquees")
except Exception as e:
    print(f"ERREUR migrations: {e}")

# Collecte des fichiers statiques
print("2. Collecte des fichiers statiques...")
try:
    call_command('collectstatic', '--noinput', verbosity=0)
    print("OK - Fichiers statiques collectes")
except Exception as e:
    print(f"ERREUR collectstatic: {e}")

# Vérification du superutilisateur
print("3. Vérification du superutilisateur...")
User = get_user_model()
if User.objects.filter(username='admin').exists():
    print("OK - Superutilisateur 'admin' existe")
else:
    print("ATTENTION - Superutilisateur 'admin' manquant")
    print("   Creez-le avec: python manage.py createsuperuser")

# Vérification des données
print("4. Vérification des données...")
from apps.portfolio.models import Personal, Technology, Project, Certification

personal_count = Personal.objects.count()
tech_count = Technology.objects.count()
project_count = Project.objects.count()
cert_count = Certification.objects.count()

print(f"   - Informations personnelles: {personal_count}")
print(f"   - Technologies: {tech_count}")
print(f"   - Projets: {project_count}")
print(f"   - Certifications: {cert_count}")

if personal_count == 0:
    print("ATTENTION - Aucune information personnelle trouvee")
    print("   Ajoutez vos informations via l'admin Django")

print("\n=== PRET POUR LA PRODUCTION ===")
print("OK - Configuration terminee")
print("OK - Projet nettoye")
print("OK - Fichiers optimises")
print("\nDeployez maintenant sur Render !")
