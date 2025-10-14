#!/usr/bin/env python
"""
Script pour nettoyer et recréer les données de l'admin
"""
import os
import sys
import django

# Configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.portfolio.models import (
    Personal, About, Technology, Testimonial, BlogPost, Project, 
    ContactMessage, SiteSettings, Experience, Education, Portfolio
)

def clear_all_data():
    """Supprimer toutes les données existantes"""
    print("Suppression des donnees existantes...")
    
    # Supprimer dans l'ordre inverse des dépendances
    ContactMessage.objects.all().delete()
    BlogPost.objects.all().delete()
    Project.objects.all().delete()
    Testimonial.objects.all().delete()
    Technology.objects.all().delete()
    About.objects.all().delete()
    Personal.objects.all().delete()
    SiteSettings.objects.all().delete()
    Experience.objects.all().delete()
    Education.objects.all().delete()
    Portfolio.objects.all().delete()
    
    print("Donnees supprimees!")

def create_basic_data():
    """Créer les données de base pour l'admin"""
    print("Creation des donnees de base...")
    
    # Personal
    personal, created = Personal.objects.get_or_create(
        name="Donaldo ZOUBERY",
        defaults={
            'role': "Développeur Full-Stack & Expert DevOps",
            'mini_description': "Passionné par la création d'expériences digitales exceptionnelles",
            'cv_description': "Expert en développement web moderne avec une expertise approfondie en Python, Django, React et solutions cloud.",
            'github': "https://github.com/donaldozoubery",
            'linkedin': "https://linkedin.com/in/donaldozoubery",
            'phone': "+261 34 12 345 67",
            'email': "donaldo.zoubery@gmail.com",
            'location': "Antananarivo, Madagascar"
        }
    )
    print(f"Personal: {'Cree' if created else 'Existe deja'}")
    
    # About
    about, created = About.objects.get_or_create(
        id=1,
        defaults={
            'description': """
            <p>Je suis un développeur passionné avec plus de 5 ans d'expérience dans le développement web moderne. 
            Spécialisé dans les technologies Python/Django et JavaScript/React, je crée des solutions robustes et évolutives.</p>
            
            <p>Mon expertise couvre :</p>
            <ul>
                <li>Développement Backend avec Python, Django, FastAPI</li>
                <li>Développement Frontend avec React, Vue.js, TypeScript</li>
                <li>DevOps et Cloud avec Docker, AWS, Azure</li>
                <li>Bases de données PostgreSQL, MongoDB</li>
                <li>Architecture microservices et API REST</li>
            </ul>
            
            <p>Je suis constamment à l'affût des nouvelles technologies et j'aime relever des défis techniques complexes.</p>
            """
        }
    )
    print(f"About: {'Cree' if created else 'Existe deja'}")
    
    # Technologies
    technologies_data = [
        {'name': 'Python', 'skill_level': 95, 'is_featured': True},
        {'name': 'Django', 'skill_level': 90, 'is_featured': True},
        {'name': 'React', 'skill_level': 85, 'is_featured': True},
        {'name': 'JavaScript', 'skill_level': 90, 'is_featured': True},
        {'name': 'PostgreSQL', 'skill_level': 80, 'is_featured': True},
        {'name': 'Docker', 'skill_level': 75, 'is_featured': True},
        {'name': 'AWS', 'skill_level': 70, 'is_featured': True},
        {'name': 'Git', 'skill_level': 85, 'is_featured': True},
    ]
    
    for tech_data in technologies_data:
        tech, created = Technology.objects.get_or_create(
            name=tech_data['name'],
            defaults=tech_data
        )
        print(f"Technology {tech_data['name']}: {'Cree' if created else 'Existe deja'}")
    
    # SiteSettings
    settings, created = SiteSettings.objects.get_or_create(
        id=1,
        defaults={
            'site_name': 'Donaldo ZOUBERY - Portfolio',
            'site_description': 'Développeur Full-Stack & Expert DevOps',
            'site_url': 'https://donaldozoubery.com',
            'is_maintenance_mode': False,
            'address': 'Antananarivo, Madagascar',
            'phone': '+261 34 12 345 67',
            'email': 'donaldo.zoubery@gmail.com'
        }
    )
    print(f"SiteSettings: {'Cree' if created else 'Existe deja'}")
    
    print("Donnees de base creees!")

def main():
    """Fonction principale"""
    print("=== RESET DES DONNEES ADMIN ===")
    
    # Demander confirmation
    response = input("Voulez-vous supprimer toutes les donnees existantes? (y/N): ")
    if response.lower() != 'y':
        print("Operation annulee.")
        return
    
    clear_all_data()
    create_basic_data()
    
    print("\n=== TERMINE ===")
    print("Vous pouvez maintenant acceder a l'admin Django pour modifier les donnees.")
    print("URL Admin: http://127.0.0.1:8000/admin/")

if __name__ == '__main__':
    main()
