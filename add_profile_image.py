#!/usr/bin/env python
"""
Script pour ajouter une image de profil par défaut
Exécuter avec: python add_profile_image.py
"""

import os
import sys
import django
from PIL import Image, ImageDraw, ImageFont
import io

# Configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.portfolio.models import Personal, About
from django.core.files.base import ContentFile

def create_default_profile_image():
    """Créer une image de profil par défaut avec les initiales"""
    
    # Créer une image 400x400 avec un fond dégradé
    size = (400, 400)
    image = Image.new('RGB', size, color='#667eea')
    draw = ImageDraw.Draw(image)
    
    # Créer un dégradé simple
    for y in range(size[1]):
        color_value = int(255 * (1 - y / size[1]))
        color = (102 + color_value // 4, 126 + color_value // 4, 234 + color_value // 4)
        draw.line([(0, y), (size[0], y)], fill=color)
    
    # Ajouter un cercle blanc au centre
    circle_size = 300
    circle_pos = ((size[0] - circle_size) // 2, (size[1] - circle_size) // 2)
    draw.ellipse([circle_pos, (circle_pos[0] + circle_size, circle_pos[1] + circle_size)], 
                 fill='white', outline='#4f46e5', width=4)
    
    # Ajouter les initiales "DZ"
    try:
        # Essayer d'utiliser une police système
        font = ImageFont.truetype("arial.ttf", 80)
    except:
        try:
            font = ImageFont.truetype("Arial.ttf", 80)
        except:
            # Police par défaut
            font = ImageFont.load_default()
    
    # Calculer la position du texte
    text = "DZ"
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    text_x = (size[0] - text_width) // 2
    text_y = (size[1] - text_height) // 2 - 10
    
    # Dessiner le texte
    draw.text((text_x, text_y), text, fill='#4f46e5', font=font)
    
    # Ajouter "Développeur" en dessous
    try:
        small_font = ImageFont.truetype("arial.ttf", 20)
    except:
        try:
            small_font = ImageFont.truetype("Arial.ttf", 20)
        except:
            small_font = ImageFont.load_default()
    
    subtitle = "Développeur"
    bbox_sub = draw.textbbox((0, 0), subtitle, font=small_font)
    sub_width = bbox_sub[2] - bbox_sub[0]
    sub_x = (size[0] - sub_width) // 2
    sub_y = text_y + text_height + 20
    
    draw.text((sub_x, sub_y), subtitle, fill='#6b7280', font=small_font)
    
    # Sauvegarder l'image en mémoire
    img_buffer = io.BytesIO()
    image.save(img_buffer, format='PNG')
    img_buffer.seek(0)
    
    return img_buffer

def add_profile_images():
    """Ajouter des images de profil aux modèles Personal et About"""
    
    print("Creation des images de profil par defaut...")
    
    # Créer l'image
    img_buffer = create_default_profile_image()
    
    # Ajouter l'image au modèle Personal
    personal_objects = Personal.objects.all()
    for personal in personal_objects:
        if not personal.photo:
            personal.photo.save(
                'default_profile.png',
                ContentFile(img_buffer.getvalue()),
                save=True
            )
            print(f"Image ajoutee pour: {personal.name}")
    
    # Réinitialiser le buffer pour About
    img_buffer.seek(0)
    
    # Ajouter l'image au modèle About
    about_objects = About.objects.all()
    for about in about_objects:
        if not about.photo:
            about.photo.save(
                'default_about.png',
                ContentFile(img_buffer.getvalue()),
                save=True
            )
            print(f"Image ajoutee pour About")
    
    print("Images de profil creees avec succes!")

if __name__ == '__main__':
    add_profile_images()
