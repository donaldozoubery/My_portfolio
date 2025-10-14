#!/usr/bin/env python
"""
Script pour créer les images manquantes
"""
import os
from PIL import Image, ImageDraw, ImageFont
import random

def create_hero_bg():
    """Créer l'image de fond hero"""
    # Créer une image de fond dégradé
    width, height = 1920, 1080
    image = Image.new('RGB', (width, height))
    
    # Créer un dégradé
    for y in range(height):
        # Dégradé du bleu foncé au violet
        r = int(15 + (y / height) * 30)  # 15 à 45
        g = int(15 + (y / height) * 20)  # 15 à 35
        b = int(35 + (y / height) * 50)  # 35 à 85
        
        for x in range(width):
            image.putpixel((x, y), (r, g, b))
    
    # Ajouter des particules/étoiles
    draw = ImageDraw.Draw(image)
    for _ in range(100):
        x = random.randint(0, width)
        y = random.randint(0, height)
        size = random.randint(1, 3)
        alpha = random.randint(50, 150)
        color = (255, 255, 255, alpha)
        draw.ellipse([x-size, y-size, x+size, y+size], fill=color)
    
    # Sauvegarder
    os.makedirs('static/assets/img', exist_ok=True)
    image.save('static/assets/img/hero-bg.jpg', 'JPEG', quality=90)
    print("Image hero-bg.jpg creee")

def create_profile_image():
    """Créer une image de profil par défaut"""
    # Créer une image de profil
    size = 400
    image = Image.new('RGB', (size, size), color=(99, 102, 241))  # Couleur primaire
    
    # Créer un dégradé circulaire
    draw = ImageDraw.Draw(image)
    
    # Dégradé du centre vers l'extérieur
    for i in range(size // 2):
        alpha = int(255 * (1 - i / (size // 2)))
        color = (99 + i, 102 + i, 241 + i)
        draw.ellipse([i, i, size-i, size-i], outline=color, width=2)
    
    # Ajouter un cercle central
    center = size // 2
    radius = size // 4
    draw.ellipse([center-radius, center-radius, center+radius, center+radius], 
                 fill=(255, 255, 255, 100), outline=(255, 255, 255), width=3)
    
    # Ajouter des initiales "DZ"
    try:
        font = ImageFont.truetype("arial.ttf", 80)
    except:
        font = ImageFont.load_default()
    
    text = "DZ"
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    x = (size - text_width) // 2
    y = (size - text_height) // 2
    
    draw.text((x, y), text, fill=(255, 255, 255), font=font)
    
    # Sauvegarder
    os.makedirs('static/assets/img', exist_ok=True)
    image.save('static/assets/img/profile.jpg', 'JPEG', quality=95)
    print("Image profile.jpg creee")

def main():
    """Créer toutes les images manquantes"""
    print("Creation des images manquantes...")
    
    create_hero_bg()
    create_profile_image()
    
    print("Toutes les images ont ete creees !")

if __name__ == '__main__':
    main()
