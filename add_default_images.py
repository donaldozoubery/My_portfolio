#!/usr/bin/env python
"""
Script pour ajouter des images par défaut aux projets et articles de blog
Exécuter avec: python add_default_images.py
"""

import os
import sys
import django
from PIL import Image, ImageDraw, ImageFont
import io

# Configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.portfolio.models import Project, BlogPost
from django.core.files.base import ContentFile

def create_project_image(project_name, project_type="web"):
    """Créer une image de projet par défaut"""
    
    # Créer une image 400x200 avec un fond dégradé
    size = (400, 200)
    
    # Couleurs selon le type de projet
    if project_type == "web":
        colors = ['#667eea', '#764ba2']
        icon = "🌐"
    elif project_type == "mobile":
        colors = ['#f093fb', '#f5576c']
        icon = "📱"
    elif project_type == "devops":
        colors = ['#4facfe', '#00f2fe']
        icon = "⚙️"
    else:
        colors = ['#43e97b', '#38f9d7']
        icon = "💻"
    
    image = Image.new('RGB', size, color=colors[0])
    draw = ImageDraw.Draw(image)
    
    # Créer un dégradé simple
    for y in range(size[1]):
        color_value = int(255 * (1 - y / size[1]))
        r = int(colors[0][1:3], 16) + color_value // 4
        g = int(colors[0][3:5], 16) + color_value // 4
        b = int(colors[0][5:7], 16) + color_value // 4
        r = min(255, r)
        g = min(255, g)
        b = min(255, b)
        color = (r, g, b)
        draw.line([(0, y), (size[0], y)], fill=color)
    
    # Ajouter un cercle blanc au centre
    circle_size = 80
    circle_pos = ((size[0] - circle_size) // 2, (size[1] - circle_size) // 2 - 10)
    draw.ellipse([circle_pos, (circle_pos[0] + circle_size, circle_pos[1] + circle_size)], 
                 fill='white', outline='#4f46e5', width=3)
    
    # Ajouter l'icône
    try:
        font = ImageFont.truetype("arial.ttf", 40)
    except:
        try:
            font = ImageFont.truetype("Arial.ttf", 40)
        except:
            font = ImageFont.load_default()
    
    # Calculer la position de l'icône
    text = icon
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    text_x = (size[0] - text_width) // 2
    text_y = (size[1] - text_height) // 2 - 10
    
    draw.text((text_x, text_y), text, fill='#4f46e5', font=font)
    
    # Ajouter le nom du projet en dessous
    try:
        small_font = ImageFont.truetype("arial.ttf", 16)
    except:
        try:
            small_font = ImageFont.truetype("Arial.ttf", 16)
        except:
            small_font = ImageFont.load_default()
    
    # Tronquer le nom s'il est trop long
    display_name = project_name[:20] + "..." if len(project_name) > 20 else project_name
    bbox_sub = draw.textbbox((0, 0), display_name, font=small_font)
    sub_width = bbox_sub[2] - bbox_sub[0]
    sub_x = (size[0] - sub_width) // 2
    sub_y = text_y + text_height + 20
    
    draw.text((sub_x, sub_y), display_name, fill='#6b7280', font=small_font)
    
    # Sauvegarder l'image en mémoire
    img_buffer = io.BytesIO()
    image.save(img_buffer, format='PNG')
    img_buffer.seek(0)
    
    return img_buffer

def create_blog_image(blog_title, blog_type="tech"):
    """Créer une image d'article de blog par défaut"""
    
    # Créer une image 400x200 avec un fond dégradé
    size = (400, 200)
    
    # Couleurs selon le type d'article
    if blog_type == "tech":
        colors = ['#10b981', '#059669']
        icon = "📝"
    elif blog_type == "tutorial":
        colors = ['#f59e0b', '#d97706']
        icon = "🎓"
    elif blog_type == "news":
        colors = ['#ef4444', '#dc2626']
        icon = "📰"
    else:
        colors = ['#8b5cf6', '#7c3aed']
        icon = "💡"
    
    image = Image.new('RGB', size, color=colors[0])
    draw = ImageDraw.Draw(image)
    
    # Créer un dégradé simple
    for y in range(size[1]):
        color_value = int(255 * (1 - y / size[1]))
        r = int(colors[0][1:3], 16) + color_value // 4
        g = int(colors[0][3:5], 16) + color_value // 4
        b = int(colors[0][5:7], 16) + color_value // 4
        r = min(255, r)
        g = min(255, g)
        b = min(255, b)
        color = (r, g, b)
        draw.line([(0, y), (size[0], y)], fill=color)
    
    # Ajouter un rectangle blanc au centre
    rect_size = (300, 100)
    rect_pos = ((size[0] - rect_size[0]) // 2, (size[1] - rect_size[1]) // 2 - 10)
    draw.rectangle([rect_pos, (rect_pos[0] + rect_size[0], rect_pos[1] + rect_size[1])], 
                   fill='white', outline='#059669', width=3)
    
    # Ajouter l'icône
    try:
        font = ImageFont.truetype("arial.ttf", 30)
    except:
        try:
            font = ImageFont.truetype("Arial.ttf", 30)
        except:
            font = ImageFont.load_default()
    
    # Calculer la position de l'icône
    text = icon
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    text_x = (size[0] - text_width) // 2
    text_y = (size[1] - text_height) // 2 - 20
    
    draw.text((text_x, text_y), text, fill='#059669', font=font)
    
    # Ajouter le titre de l'article en dessous
    try:
        small_font = ImageFont.truetype("arial.ttf", 14)
    except:
        try:
            small_font = ImageFont.truetype("Arial.ttf", 14)
        except:
            small_font = ImageFont.load_default()
    
    # Tronquer le titre s'il est trop long
    display_title = blog_title[:25] + "..." if len(blog_title) > 25 else blog_title
    bbox_sub = draw.textbbox((0, 0), display_title, font=small_font)
    sub_width = bbox_sub[2] - bbox_sub[0]
    sub_x = (size[0] - sub_width) // 2
    sub_y = text_y + text_height + 10
    
    draw.text((sub_x, sub_y), display_title, fill='#6b7280', font=small_font)
    
    # Sauvegarder l'image en mémoire
    img_buffer = io.BytesIO()
    image.save(img_buffer, format='PNG')
    img_buffer.seek(0)
    
    return img_buffer

def add_default_images():
    """Ajouter des images par défaut aux projets et articles de blog"""
    
    print("Creation des images par defaut pour projets et articles...")
    
    # Ajouter des images aux projets
    projects = Project.objects.all()
    for project in projects:
        if not project.featured_image:
            # Déterminer le type de projet
            if "mobile" in project.name.lower() or "app" in project.name.lower():
                project_type = "mobile"
            elif "devops" in project.name.lower() or "monitoring" in project.name.lower():
                project_type = "devops"
            else:
                project_type = "web"
            
            img_buffer = create_project_image(project.name, project_type)
            project.featured_image.save(
                f'project_{project.id}_default.png',
                ContentFile(img_buffer.getvalue()),
                save=True
            )
            print(f"Image ajoutee pour le projet: {project.name}")
    
    # Ajouter des images aux articles de blog
    blog_posts = BlogPost.objects.all()
    for post in blog_posts:
        if not post.featured_image:
            # Déterminer le type d'article
            if "tutorial" in post.title.lower() or "guide" in post.title.lower():
                blog_type = "tutorial"
            elif "news" in post.title.lower() or "actualité" in post.title.lower():
                blog_type = "news"
            else:
                blog_type = "tech"
            
            img_buffer = create_blog_image(post.title, blog_type)
            post.featured_image.save(
                f'blog_{post.id}_default.png',
                ContentFile(img_buffer.getvalue()),
                save=True
            )
            print(f"Image ajoutee pour l'article: {post.title}")
    
    print("Images par defaut creees avec succes!")

if __name__ == '__main__':
    add_default_images()
