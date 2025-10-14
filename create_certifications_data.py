#!/usr/bin/env python
"""
Script pour créer des données de démonstration des certifications
"""
import os
import sys
import django
from datetime import date, timedelta

# Configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.portfolio.models import Certification, Technology

def create_certifications_data():
    """Créer des données de démonstration pour les certifications"""
    print("=== CREATION DES DONNEES CERTIFICATIONS ===")
    
    # Récupérer quelques technologies pour les associer
    technologies = list(Technology.objects.all()[:10])
    
    certifications_data = [
        {
            'title': 'AWS Certified Solutions Architect',
            'issuing_organization': 'Amazon Web Services',
            'credential_id': 'AWS-SAA-2024-001',
            'credential_url': 'https://aws.amazon.com/verification',
            'issue_date': date(2024, 1, 15),
            'expiry_date': date(2026, 1, 15),
            'description': 'Certification professionnelle pour concevoir et déployer des applications évolutives sur AWS.',
            'skills': ['AWS', 'Docker', 'Linux'],
            'is_featured': True,
            'is_verified': True,
            'order': 1
        },
        {
            'title': 'Django Web Development',
            'issuing_organization': 'Django Software Foundation',
            'credential_id': 'DJANGO-2024-002',
            'credential_url': 'https://djangoproject.com/certification',
            'issue_date': date(2023, 11, 20),
            'expiry_date': None,
            'description': 'Certification en développement web avec Django, framework Python puissant.',
            'skills': ['Django', 'Python', 'PostgreSQL'],
            'is_featured': True,
            'is_verified': True,
            'order': 2
        },
        {
            'title': 'React Developer Certification',
            'issuing_organization': 'Meta (Facebook)',
            'credential_id': 'REACT-2024-003',
            'credential_url': 'https://react.dev/certification',
            'issue_date': date(2023, 9, 10),
            'expiry_date': date(2025, 9, 10),
            'description': 'Certification officielle pour le développement d\'interfaces utilisateur avec React.',
            'skills': ['React', 'JavaScript', 'HTML5', 'CSS3'],
            'is_featured': True,
            'is_verified': True,
            'order': 3
        },
        {
            'title': 'Docker Certified Associate',
            'issuing_organization': 'Docker Inc.',
            'credential_id': 'DCA-2024-004',
            'credential_url': 'https://docker.com/certification',
            'issue_date': date(2024, 2, 28),
            'expiry_date': date(2026, 2, 28),
            'description': 'Certification pour la containerisation et l\'orchestration avec Docker.',
            'skills': ['Docker', 'Linux', 'DevOps'],
            'is_featured': True,
            'is_verified': True,
            'order': 4
        },
        {
            'title': 'Python Programming Professional',
            'issuing_organization': 'Python Institute',
            'credential_id': 'PCPP-2024-005',
            'credential_url': 'https://pythoninstitute.org/certification',
            'issue_date': date(2023, 12, 5),
            'expiry_date': None,
            'description': 'Certification avancée en programmation Python pour le développement professionnel.',
            'skills': ['Python', 'Git', 'Node.js'],
            'is_featured': True,
            'is_verified': True,
            'order': 5
        },
        {
            'title': 'Frontend Web Development',
            'issuing_organization': 'FreeCodeCamp',
            'credential_id': 'FCC-FE-2024-006',
            'credential_url': 'https://freecodecamp.org/certification',
            'issue_date': date(2023, 8, 15),
            'expiry_date': None,
            'description': 'Certification complète en développement frontend moderne.',
            'skills': ['HTML5', 'CSS3', 'JavaScript', 'Tailwind CSS'],
            'is_featured': True,
            'is_verified': True,
            'order': 6
        }
    ]
    
    created_count = 0
    
    for cert_data in certifications_data:
        # Créer la certification
        cert, created = Certification.objects.get_or_create(
            title=cert_data['title'],
            defaults={
                'issuing_organization': cert_data['issuing_organization'],
                'credential_id': cert_data['credential_id'],
                'credential_url': cert_data['credential_url'],
                'issue_date': cert_data['issue_date'],
                'expiry_date': cert_data['expiry_date'],
                'description': cert_data['description'],
                'is_featured': cert_data['is_featured'],
                'is_verified': cert_data['is_verified'],
                'order': cert_data['order']
            }
        )
        
        if created:
            # Associer les compétences
            for skill_name in cert_data['skills']:
                try:
                    skill = Technology.objects.get(name__icontains=skill_name)
                    cert.skills.add(skill)
                except Technology.DoesNotExist:
                    print(f"Compétence '{skill_name}' non trouvée pour {cert.title}")
            
            print(f"Certification créée: {cert.title}")
            created_count += 1
        else:
            print(f"Certification existe déjà: {cert.title}")
    
    print(f"\n=== RESUME ===")
    print(f"Certifications créées: {created_count}")
    print(f"Total certifications: {Certification.objects.count()}")
    
    print(f"\n=== CERTIFICATIONS DISPONIBLES ===")
    for cert in Certification.objects.all().order_by('order'):
        print(f"- {cert.title} ({cert.issuing_organization}) - {cert.status}")

if __name__ == '__main__':
    create_certifications_data()
