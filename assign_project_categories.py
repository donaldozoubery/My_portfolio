#!/usr/bin/env python
"""
Script pour assigner des catégories aux projets existants
"""
import os
import sys
import django

# Configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.portfolio.models import Project

def assign_project_categories():
    """Assigner des catégories aux projets existants"""
    print("=== ASSIGNATION DES CATEGORIES PROJETS ===")
    
    # Mapping des projets vers leurs catégories
    project_categories = {
        'Portfolio Django': 'web',
        'E-commerce React': 'web',
        'API REST Node.js': 'web',
        'Application Mobile Flutter': 'mobile',
        'Dashboard Analytics': 'web',
        'Système de Gestion': 'desktop',
        'Déploiement Docker': 'devops',
        'Chatbot IA': 'ai',
        'Application Desktop Python': 'desktop',
        'Site Vitrine': 'web',
        'Application Mobile React Native': 'mobile',
        'API GraphQL': 'web',
        'Système de Monitoring': 'devops',
        'Reconnaissance d\'Images': 'ai',
        'Application Desktop Electron': 'desktop',
        'Plateforme E-learning': 'web',
        'Application Mobile Ionic': 'mobile',
        'Infrastructure Cloud': 'devops'
    }
    
    updated_count = 0
    
    for project in Project.objects.all():
        if project.name in project_categories:
            old_category = project.category
            project.category = project_categories[project.name]
            project.save()
            print(f"{project.name}: {old_category} -> {project.category}")
            updated_count += 1
        else:
            print(f"{project.name}: Pas de catégorie spécifique trouvée (garde: {project.category})")
    
    print(f"\n=== RESUME ===")
    print(f"Projets mis à jour: {updated_count}")
    print(f"Total projets: {Project.objects.count()}")
    
    print(f"\n=== PROJETS PAR CATEGORIE ===")
    categories = ['web', 'mobile', 'desktop', 'devops', 'ai', 'other']
    for category in categories:
        count = Project.objects.filter(category=category).count()
        print(f"- {category}: {count} projets")

if __name__ == '__main__':
    assign_project_categories()
