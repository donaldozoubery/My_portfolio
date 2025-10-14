#!/usr/bin/env python
"""
Script de test pour vérifier le système de thème
"""
import os
import sys
import django

# Configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.test import Client
from django.contrib.sessions.models import Session

def test_theme_system():
    """Test du système de thème"""
    print("Test du systeme de theme Django...")
    
    client = Client()
    
    # Test 1: Page d'accueil
    print("1. Test de la page d'accueil...")
    response = client.get('/')
    print(f"   Status: {response.status_code}")
    print(f"   Theme par defaut: {'dark' if 'dark' in response.content.decode() else 'light'}")
    
    # Test 2: Toggle theme
    print("2. Test du toggle theme...")
    response = client.post('/toggle-theme/', HTTP_X_REQUESTED_WITH='XMLHttpRequest')
    print(f"   Status: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        print(f"   Nouveau theme: {data.get('theme')}")
        print(f"   Icone: {data.get('icon')}")
    
    # Test 3: Verification du theme
    print("3. Test de recuperation du theme...")
    response = client.get('/get-theme/')
    print(f"   Status: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        print(f"   Theme actuel: {data.get('theme')}")
        print(f"   Icone: {data.get('icon')}")
    
    print("Test termine!")

if __name__ == '__main__':
    test_theme_system()
