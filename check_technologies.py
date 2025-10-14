#!/usr/bin/env python
"""
Script pour vérifier les technologies
"""
import os
import sys
import django

# Configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.portfolio.models import Technology

def check_technologies():
    """Vérifier les technologies"""
    print("=== VERIFICATION DES TECHNOLOGIES ===")
    
    total_techs = Technology.objects.count()
    featured_techs = Technology.objects.filter(is_featured=True).count()
    
    print(f"Total des technologies: {total_techs}")
    print(f"Technologies featured: {featured_techs}")
    print(f"Technologies non-featured: {total_techs - featured_techs}")
    
    print("\n=== TECHNOLOGIES FEATURED ===")
    for tech in Technology.objects.filter(is_featured=True):
        print(f"- {tech.name} (niveau: {tech.skill_level}%)")
    
    print("\n=== TECHNOLOGIES NON-FEATURED ===")
    for tech in Technology.objects.filter(is_featured=False):
        print(f"- {tech.name} (niveau: {tech.skill_level}%)")

if __name__ == '__main__':
    check_technologies()
