#!/usr/bin/env python
"""
Script pour corriger les technologies
"""
import os
import sys
import django

# Configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.portfolio.models import Technology

def fix_technologies():
    """Corriger les technologies"""
    print("=== CORRECTION DES TECHNOLOGIES ===")
    
    # 1. Marquer toutes les technologies comme featured
    updated_count = Technology.objects.filter(is_featured=False).update(is_featured=True)
    print(f"Technologies marquees comme featured: {updated_count}")
    
    # 2. Supprimer les doublons
    seen_names = set()
    duplicates = []
    
    for tech in Technology.objects.all().order_by('id'):
        if tech.name in seen_names:
            duplicates.append(tech)
        else:
            seen_names.add(tech.name)
    
    print(f"Doublons trouves: {len(duplicates)}")
    for dup in duplicates:
        print(f"- Suppression: {dup.name} (ID: {dup.id})")
        dup.delete()
    
    # 3. Mettre à jour les niveaux de compétence
    tech_levels = {
        'Python': 95,
        'Django': 90,
        'JavaScript': 90,
        'React': 85,
        'HTML5': 95,
        'CSS3': 90,
        'PostgreSQL': 85,
        'Docker': 90,
        'AWS': 85,
        'Linux': 90,
        'Git': 85,
        'Node.js': 80,
        'Redis': 80,
        'Figma': 75,
        'Tailwind CSS': 85,
        'Trello': 70,
        'MySQL': 80,
        'PHP': 60
    }
    
    print("\n=== MISE A JOUR DES NIVEAUX ===")
    for tech in Technology.objects.all():
        if tech.name in tech_levels:
            old_level = tech.skill_level
            tech.skill_level = tech_levels[tech.name]
            tech.save()
            print(f"{tech.name}: {old_level}% -> {tech.skill_level}%")
    
    print("\n=== RESUME FINAL ===")
    total = Technology.objects.count()
    featured = Technology.objects.filter(is_featured=True).count()
    print(f"Total technologies: {total}")
    print(f"Technologies featured: {featured}")
    
    print("\n=== TECHNOLOGIES FINALES ===")
    for tech in Technology.objects.filter(is_featured=True).order_by('-skill_level'):
        print(f"- {tech.name}: {tech.skill_level}%")

if __name__ == '__main__':
    fix_technologies()
