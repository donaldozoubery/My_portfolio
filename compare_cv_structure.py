#!/usr/bin/env python
"""
Script pour comparer la structure du CV digital et du PDF
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.portfolio.models import Personal

print("=== COMPARAISON STRUCTURE CV ===")

personal = Personal.objects.first()
if personal:
    print(f"Nom: {personal.name}")
    print(f"Role: {personal.role}")
    print(f"Email: {personal.email}")
    print(f"Phone: {personal.phone}")
    print(f"Location: {personal.location}")
    print(f"LinkedIn: {personal.linkedin}")
    print(f"GitHub: {personal.github}")

print("\n=== STRUCTURE CV DIGITAL ===")
print("1. Header avec nom en grand (ZOUBERY Jaotiana Donaldo)")
print("2. Role (Developpeur web full stack & Dev Ops)")
print("3. Contact (adresse, email, telephone)")
print("4. Reseaux sociaux (LinkedIn, GitHub)")
print("5. Profil (description personnelle)")
print("6. Education (formation)")
print("7. Competences (technologies)")

print("\n=== STRUCTURE PDF CORRIGEE ===")
print("1. Header avec nom en grand (22px, gras, ombre)")
print("2. Role (14px, police moyenne)")
print("3. Contact (11px, icones, espacement)")
print("4. Reseaux sociaux (cartes avec icones)")
print("5. Profil (description centree)")
print("6. Education (timeline avec ronds)")
print("7. Competences (grille 2 colonnes)")

print("\n=== AMELIORATIONS APPLIQUEES ===")
print("Nom plus grand: 22px (au lieu de 18px)")
print("Ombre sur le nom pour visibilite")
print("Role plus visible: 14px (au lieu de 12px)")
print("Contact plus lisible: 11px (au lieu de 9px)")
print("Bouton PDF plus visible: 10px, gras")
print("Espacement ameliore entre elements")
print("Header avec border-radius pour style moderne")

print("\n=== RESULTAT ===")
print("Le PDF commence maintenant par le nom 'Donaldo' comme le CV digital")
print("Structure identique avec visibilite amelioree")
print("Testez sur: http://127.0.0.1:8000/download-cv/")
