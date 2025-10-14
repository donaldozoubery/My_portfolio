#!/usr/bin/env python
"""
Script pour créer des données de démonstration pour la roadmap
"""
import os
import sys
import django
from datetime import date, datetime

# Configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.portfolio.models import RoadmapStep, Technology

def create_roadmap_data():
    """Créer des données de démonstration pour la roadmap"""
    print("Creation des donnees de roadmap...")
    
    # Récupérer quelques technologies existantes
    technologies = list(Technology.objects.all()[:10])
    
    # Données de la roadmap
    roadmap_data = [
        {
            'title': 'Développeur Full-Stack Senior',
            'description': 'Développement d\'applications web complexes avec Django et React. Gestion d\'équipes de développement et architecture de solutions scalables.',
            'step_type': 'experience',
            'start_date': date(2023, 1, 1),
            'end_date': None,
            'is_current': True,
            'is_featured': True,
            'icon': 'fas fa-laptop-code',
            'color': '#6366f1',
            'order': 1,
            'skills': technologies[:5]
        },
        {
            'title': 'Certification AWS Solutions Architect',
            'description': 'Obtention de la certification AWS Solutions Architect Associate. Expertise en architecture cloud et services AWS.',
            'step_type': 'certification',
            'start_date': date(2022, 11, 15),
            'end_date': date(2022, 12, 20),
            'is_current': False,
            'is_featured': True,
            'icon': 'fas fa-certificate',
            'color': '#ff9500',
            'order': 2,
            'skills': technologies[2:4]
        },
        {
            'title': 'Projet E-commerce Multi-vendeur',
            'description': 'Développement d\'une plateforme e-commerce complète avec système de paiement, gestion des commandes et interface d\'administration.',
            'step_type': 'project',
            'start_date': date(2022, 6, 1),
            'end_date': date(2022, 10, 30),
            'is_current': False,
            'is_featured': True,
            'icon': 'fas fa-shopping-cart',
            'color': '#10b981',
            'order': 3,
            'skills': technologies[:6]
        },
        {
            'title': 'Formation React Avancé',
            'description': 'Formation intensive sur React, Redux, et les patterns avancés. Développement d\'applications SPA performantes.',
            'step_type': 'education',
            'start_date': date(2022, 3, 1),
            'end_date': date(2022, 5, 31),
            'is_current': False,
            'is_featured': True,
            'icon': 'fas fa-graduation-cap',
            'color': '#8b5cf6',
            'order': 4,
            'skills': technologies[1:3]
        },
        {
            'title': 'Développeur Python/Django',
            'description': 'Spécialisation en développement backend avec Python et Django. Création d\'APIs REST et intégration de bases de données.',
            'step_type': 'experience',
            'start_date': date(2021, 9, 1),
            'end_date': date(2022, 12, 31),
            'is_current': False,
            'is_featured': True,
            'icon': 'fas fa-code',
            'color': '#06b6d4',
            'order': 5,
            'skills': technologies[0:4]
        },
        {
            'title': 'Premier Projet Open Source',
            'description': 'Création et publication de ma première bibliothèque Python sur GitHub. Contribution à la communauté open source.',
            'step_type': 'achievement',
            'start_date': date(2021, 6, 15),
            'end_date': date(2021, 8, 30),
            'is_current': False,
            'is_featured': True,
            'icon': 'fas fa-star',
            'color': '#f59e0b',
            'order': 6,
            'skills': technologies[0:2]
        },
        {
            'title': 'Formation Développement Web',
            'description': 'Formation complète en développement web : HTML, CSS, JavaScript, Python, et bases de données. Premiers pas dans le développement.',
            'step_type': 'education',
            'start_date': date(2021, 1, 1),
            'end_date': date(2021, 5, 31),
            'is_current': False,
            'is_featured': True,
            'icon': 'fas fa-book',
            'color': '#ef4444',
            'order': 7,
            'skills': technologies[0:3]
        },
        {
            'title': 'Début du Parcours Tech',
            'description': 'Découverte de la programmation et premiers projets personnels. Passion naissante pour le développement et l\'innovation technologique.',
            'step_type': 'milestone',
            'start_date': date(2020, 9, 1),
            'end_date': date(2020, 12, 31),
            'is_current': False,
            'is_featured': True,
            'icon': 'fas fa-rocket',
            'color': '#8b5cf6',
            'order': 8,
            'skills': technologies[0:1]
        }
    ]
    
    # Créer les étapes de la roadmap
    for step_data in roadmap_data:
        # Extraire les skills avant de créer l'objet
        skills_data = step_data.pop('skills', [])
        
        step, created = RoadmapStep.objects.get_or_create(
            title=step_data['title'],
            defaults=step_data
        )
        
        if created and skills_data:
            step.skills.set(skills_data)
        
        print(f"RoadmapStep '{step_data['title']}': {'Cree' if created else 'Existe deja'}")
    
    print("Donnees de roadmap creees!")

if __name__ == '__main__':
    create_roadmap_data()
