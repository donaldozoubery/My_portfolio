#!/usr/bin/env python
"""
Script pour corriger l'icône MySQL
"""
import os
import sys
import django

# Configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.portfolio.models import Technology

def fix_mysql_icon():
    """Corriger l'icône MySQL"""
    mysql_tech = Technology.objects.get(name='My SQL')
    mysql_tech.icon = 'fas fa-database'
    mysql_tech.save()
    print(f"MySQL icône mise à jour: {mysql_tech.icon}")

if __name__ == '__main__':
    fix_mysql_icon()
