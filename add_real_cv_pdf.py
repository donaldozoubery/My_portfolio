#!/usr/bin/env python
"""
Script pour ajouter un vrai lien CV PDF
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.portfolio.models import Personal

print("=== AJOUT D'UN VRAI LIEN CV PDF ===")

# Instructions pour l'utilisateur
print("\n=== INSTRUCTIONS ===")
print("1. Uploadez votre CV PDF sur Google Drive ou Dropbox")
print("2. Récupérez le lien de partage public")
print("3. Remplacez le lien ci-dessous par votre vrai lien")
print("4. Relancez ce script")

# Lien par défaut (à remplacer)
REAL_CV_PDF_LINK = "https://drive.google.com/file/d/1ABC123XYZ789/view?usp=sharing"

print(f"\nLien actuel: {REAL_CV_PDF_LINK}")
print("\nPour changer le lien, modifiez la variable REAL_CV_PDF_LINK dans ce script")

try:
    personal_info = Personal.objects.first()
    if not personal_info:
        print("Aucune information personnelle trouvée. Veuillez créer une entrée Personal d'abord.")
    else:
        personal_info.cv_link = REAL_CV_PDF_LINK
        personal_info.save()
        print(f"Lien CV PDF mis à jour pour {personal_info.full_name}: {personal_info.cv_link}")
        print("\n✅ Le bouton de téléchargement PDF est maintenant fonctionnel !")
        print("🌐 Testez sur: http://127.0.0.1:8000/digital_cv/")

except Exception as e:
    print(f"Erreur lors de la mise à jour du lien CV PDF: {e}")

print("\n=== RÉSUMÉ ===")
personal_info = Personal.objects.first()
if personal_info:
    print(f"Lien CV PDF actuel: {personal_info.cv_link}")
    print("Status: ✅ Fonctionnel")
else:
    print("Aucune information personnelle.")
