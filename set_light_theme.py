#!/usr/bin/env python
"""
Script pour définir le thème clair par défaut
"""
import os
import sys
import django

# Configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.sessions.models import Session
from django.contrib.sessions.backends.db import SessionStore

def set_default_theme():
    """Définir le thème clair par défaut"""
    print("Definition du theme clair par defaut...")
    
    # Créer une session avec le thème clair
    session = SessionStore()
    session['theme'] = 'light'
    session.save()
    
    print("Theme clair defini par defaut!")
    print("Rechargez la page pour voir le changement.")

if __name__ == '__main__':
    set_default_theme()
