#!/usr/bin/env python
"""
Script pour corriger MySQL
"""
import os
import sys
import django

# Configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.portfolio.models import Technology

def fix_mysql():
    """Corriger MySQL"""
    mysql_tech = Technology.objects.get(name='My SQL')
    mysql_tech.skill_level = 80
    mysql_tech.save()
    print(f"MySQL niveau mis à jour: {mysql_tech.skill_level}%")

if __name__ == '__main__':
    fix_mysql()
