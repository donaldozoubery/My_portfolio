import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.portfolio.models import Personal

print("=== AJOUT DU LIEN CV PDF ===")

# Mettre à jour le lien CV PDF
personal_info, created = Personal.objects.get_or_create(
    id=1,
    defaults={
        'name': 'Donaldo ZOUBERY',
        'role': 'Développeur Full-Stack',
        'mini_description': 'Développeur passionné spécialisé dans les technologies web modernes',
        'cv_description': 'Ingénieur de support technologique expérimenté avec une solide expérience en développement web full-stack',
        'cv_link': 'https://drive.google.com/file/d/1ABC123XYZ789/view?usp=sharing',  # Remplacez par votre vrai lien
        'github': 'https://github.com/donaldozoubery',
        'linkedin': 'https://linkedin.com/in/donaldozoubery',
        'email': 'donaldo.zoubery@gmail.com',
        'phone': '+261 34 12 345 67',
        'location': 'Diégo-Suarez, Madagascar'
    }
)

if not created:
    # Mettre à jour le lien CV existant
    personal_info.cv_link = 'https://drive.google.com/file/d/1ABC123XYZ789/view?usp=sharing'  # Remplacez par votre vrai lien
    personal_info.save()
    print(f"Lien CV mis à jour pour {personal_info.name}")
else:
    print(f"Profil créé pour {personal_info.name}")

print(f"Lien CV: {personal_info.cv_link}")
print("\n=== INSTRUCTIONS ===")
print("1. Remplacez le lien dans le code par votre vrai lien Google Drive ou Dropbox")
print("2. Assurez-vous que le fichier PDF est accessible publiquement")
print("3. Le bouton PDF dans le CV digital sera maintenant fonctionnel")
