#!/usr/bin/env python
"""
Script pour tester la génération PDF
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.template.loader import render_to_string
from django.test import RequestFactory
from apps.portfolio.views import download_cv_pdf
from apps.portfolio.models import Personal, About, Experience, Education, Technology, Project, Certification

print("=== TEST DE GÉNÉRATION PDF ===")

# Créer une requête factice
factory = RequestFactory()
request = factory.get('/download-cv/')

try:
    # Tester la génération PDF
    response = download_cv_pdf(request)
    
    if response.status_code == 200:
        print("SUCCESS: Generation PDF reussie !")
        print(f"Taille du PDF: {len(response.content)} bytes")
        print(f"Content-Type: {response['Content-Type']}")
        print(f"Filename: {response['Content-Disposition']}")
        
        # Sauvegarder le PDF pour test
        with open('test_cv.pdf', 'wb') as f:
            f.write(response.content)
        print("PDF sauvegarde comme 'test_cv.pdf'")
        
    else:
        print(f"ERREUR: Status {response.status_code}")
        
except Exception as e:
    print(f"ERREUR lors de la generation: {e}")
    print("\n=== DIAGNOSTIC ===")
    
    # Vérifier les données
    personal = Personal.objects.first()
    print(f"Personal: {personal is not None}")
    if personal:
        print(f"  - Nom: {personal.name}")
        print(f"  - Email: {personal.email}")
    
    about = About.objects.first()
    print(f"About: {about is not None}")
    
    experiences = Experience.objects.count()
    print(f"Experiences: {experiences}")
    
    technologies = Technology.objects.filter(is_featured=True).count()
    print(f"Technologies: {technologies}")
    
    projects = Project.objects.filter(is_featured=True).count()
    print(f"Projets: {projects}")

print("\n=== INSTRUCTIONS ===")
print("1. Testez sur: http://127.0.0.1:8000/download-cv/")
print("2. Le PDF devrait se telecharger automatiquement")
print("3. Verifiez le fichier 'test_cv.pdf' genere")
