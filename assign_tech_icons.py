#!/usr/bin/env python
"""
Script pour assigner les bonnes icônes aux technologies
"""
import os
import sys
import django

# Configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.portfolio.models import Technology

def assign_tech_icons():
    """Assigner les icônes FontAwesome aux technologies"""
    print("=== ASSIGNATION DES ICONES TECHNOLOGIES ===")
    
    # Mapping des technologies vers leurs icônes FontAwesome
    tech_icons = {
        'Python': 'fab fa-python',
        'Django': 'fab fa-python',
        'JavaScript': 'fab fa-js-square',
        'React': 'fab fa-react',
        'HTML5': 'fab fa-html5',
        'CSS3': 'fab fa-css3-alt',
        'Node.js': 'fab fa-node-js',
        'Git': 'fab fa-git-alt',
        'Docker': 'fab fa-docker',
        'AWS': 'fab fa-aws',
        'Linux': 'fab fa-linux',
        'PostgreSQL': 'fas fa-database',
        'MySQL': 'fas fa-database',
        'Redis': 'fas fa-database',
        'Figma': 'fab fa-figma',
        'Tailwind CSS': 'fab fa-css3-alt',
        'Trello': 'fab fa-trello',
        'PHP': 'fab fa-php'
    }
    
    updated_count = 0
    
    for tech in Technology.objects.all():
        if tech.name in tech_icons:
            old_icon = tech.icon
            tech.icon = tech_icons[tech.name]
            tech.save()
            print(f"{tech.name}: {old_icon} -> {tech.icon}")
            updated_count += 1
        else:
            print(f"{tech.name}: Pas d'icône spécifique trouvée (garde: {tech.icon})")
    
    print(f"\n=== RESUME ===")
    print(f"Technologies mises à jour: {updated_count}")
    print(f"Total technologies: {Technology.objects.count()}")
    
    print(f"\n=== TECHNOLOGIES AVEC ICONES ===")
    for tech in Technology.objects.all().order_by('name'):
        print(f"- {tech.name}: {tech.icon}")

if __name__ == '__main__':
    assign_tech_icons()
