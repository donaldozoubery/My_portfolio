#!/usr/bin/env python
"""
Script pour ajouter des données de test dans l'admin
"""
import os
import sys
import django
from datetime import date, datetime

# Configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.portfolio.models import (
    Personal, About, Technology, Testimonial, BlogPost, Project, 
    ContactMessage, SiteSettings
)

def add_test_data():
    """Ajouter des données de test"""
    print("Ajout des donnees de test...")
    
    # Testimonial
    testimonial, created = Testimonial.objects.get_or_create(
        client_name="Marie Dubois",
        defaults={
            'client_position': "Directrice Marketing",
            'client_company': "TechCorp",
            'content': "Donaldo a développé notre plateforme e-commerce avec une expertise remarquable. Le projet a été livré dans les temps et dépasse nos attentes.",
            'rating': 5,
            'is_featured': True
        }
    )
    print(f"Testimonial: {'Cree' if created else 'Existe deja'}")
    
    # BlogPost
    blog_post, created = BlogPost.objects.get_or_create(
        slug='meilleures-pratiques-django-2024',
        defaults={
            'title': "Les Meilleures Pratiques Django en 2024",
            'content': """
            <h2>Introduction</h2>
            <p>Django continue d'évoluer et voici les meilleures pratiques à adopter en 2024...</p>
            
            <h2>1. Structure de Projet</h2>
            <p>Organisez votre projet Django avec une architecture claire...</p>
            
            <h2>2. Sécurité</h2>
            <p>Implémentez les bonnes pratiques de sécurité...</p>
            
            <h2>Conclusion</h2>
            <p>Ces pratiques vous aideront à créer des applications Django robustes et maintenables.</p>
            """,
            'excerpt': "Découvrez les meilleures pratiques Django pour 2024 et améliorez vos compétences de développement.",
            'author': "Donaldo ZOUBERY",
            'published': True,
            'tags': "Django, Python, Web Development, Best Practices"
        }
    )
    print(f"BlogPost: {'Cree' if created else 'Existe deja'}")
    
    # Project
    project, created = Project.objects.get_or_create(
        name="Plateforme E-commerce",
        defaults={
            'description': "Développement d'une plateforme e-commerce complète avec Django et React. Gestion des commandes, paiements, et administration.",
            'short_description': "Plateforme e-commerce moderne avec Django et React",
            'status': 'completed',
            'github_url': 'https://github.com/donaldozoubery/ecommerce-platform',
            'live_url': 'https://ecommerce-demo.com',
            'start_date': date(2024, 1, 15),
            'end_date': date(2024, 3, 30),
            'is_featured': True
        }
    )
    print(f"Project: {'Cree' if created else 'Existe deja'}")
    
    # ContactMessage
    contact_msg, created = ContactMessage.objects.get_or_create(
        name="Jean Martin",
        email="jean.martin@example.com",
        defaults={
            'subject': "Demande de collaboration",
            'message': "Bonjour, je suis intéressé par vos services de développement web. Pourriez-vous me contacter pour discuter d'un projet ?",
            'phone': "+261 34 12 345 67",
            'is_read': False
        }
    )
    print(f"ContactMessage: {'Cree' if created else 'Existe deja'}")
    
    print("Donnees de test ajoutees!")

if __name__ == '__main__':
    add_test_data()
