#!/usr/bin/env python
"""
Script pour comparer les styles CV
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.template.loader import render_to_string
from apps.portfolio.models import Personal, About, Experience, Education, Technology, Project, Certification

print("=== COMPARAISON DES STYLES CV ===")

# Récupérer les données
personal_info = Personal.objects.first()
about_info = About.objects.first()
experiences = Experience.objects.all().order_by('-start_date')
educations = Education.objects.all().order_by('-start_date')
technologies = Technology.objects.filter(is_featured=True).order_by('-skill_level')[:12]
projects = Project.objects.filter(is_featured=True).order_by('-created_at')[:6]
certifications = Certification.objects.filter(is_featured=True).order_by('-issue_date')[:6]

context = {
    'personal_info': personal_info,
    'about_info': about_info,
    'experiences': experiences,
    'educations': educations,
    'technologies': technologies,
    'projects': projects,
    'certifications': certifications,
}

print("\n=== STYLE CV DIGITAL ===")
print("Template: cv_digital_pdf.html")
print("Caractéristiques:")
print("- Header avec gradient coloré")
print("- Sections avec bordures colorées")
print("- Cartes avec ombres et effets")
print("- Barres de progression pour les compétences")
print("- Design moderne et professionnel")
print("- Couleurs: #667eea (bleu), #764ba2 (violet)")

print("\n=== STYLE CV CLASSIQUE ===")
print("Template: cv_pdf.html")
print("Caractéristiques:")
print("- Header simple avec bordure")
print("- Sections basiques")
print("- Design minimaliste")
print("- Couleurs neutres")

print("\n=== DONNEES UTILISEES ===")
print(f"Personal: {personal_info.name if personal_info else 'Aucune'}")
print(f"About: {'Oui' if about_info else 'Non'}")
print(f"Experiences: {experiences.count()}")
print(f"Educations: {educations.count()}")
print(f"Technologies: {technologies.count()}")
print(f"Projets: {projects.count()}")
print(f"Certifications: {certifications.count()}")

print("\n=== RECOMMANDATION ===")
print("Le style CV Digital est maintenant utilisé pour le PDF")
print("Il reproduit fidèlement l'apparence de la page CV digital")
print("Testez sur: http://127.0.0.1:8000/download-cv/")
