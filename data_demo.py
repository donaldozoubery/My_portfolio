#!/usr/bin/env python
"""
Script de création de données de démonstration pour le portfolio
Exécuter avec: python data_demo.py
"""

import os
import sys
import django

# Configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.portfolio.models import *

def create_demo_data():
    print("Creation des donnees de demonstration...")
    
    # 1. Créer les informations personnelles
    personal, created = Personal.objects.get_or_create(
        name="Donaldo ZOUBERY",
        defaults={
            'role': "Développeur Full-Stack & Expert DevOps",
            'mini_description': "Passionné par la création d'expériences digitales exceptionnelles",
            'cv_description': """Développeur Full-Stack avec une expertise approfondie en Python, Django, React, et DevOps. 
            Passionné par l'innovation et la création de solutions technologiques modernes qui transforment les entreprises.
            
            Avec plus de 5 ans d'expérience dans le développement web et les solutions cloud, je maîtrise les technologies 
            les plus récentes et les meilleures pratiques de l'industrie. Mon approche combine créativité et expertise 
            technique pour livrer des projets qui dépassent les attentes des clients.
            
            Spécialisé dans l'architecture de systèmes robustes, l'optimisation des performances et la mise en place 
            de pipelines CI/CD efficaces.""",
            'email': "contact@donaldozoubery.com",
            'phone': "+261 34 00 000 00",
            'location': "Antananarivo, Madagascar",
            'github': "https://github.com/donaldozoubery",
            'linkedin': "https://linkedin.com/in/donaldozoubery"
        }
    )
    print(f"Informations personnelles: {'Creees' if created else 'Deja existantes'}")
    
    # 2. Créer la section À propos
    about, created = About.objects.get_or_create(
        defaults={
            'description': """<h3>À propos de moi</h3>
            <p>Je suis un développeur Full-Stack passionné par la création d'expériences digitales exceptionnelles. 
            Avec une solide expertise en développement web moderne et les technologies cloud, je transforme les idées 
            en solutions technologiques innovantes.</p>
            
            <p>Mon approche combine créativité et expertise technique pour livrer des projets qui dépassent les attentes 
            des clients. Je crois fermement que la technologie doit servir l'humain et faciliter la vie quotidienne.</p>
            
            <h4>Mes valeurs</h4>
            <ul>
                <li><strong>Innovation :</strong> Toujours à la recherche des dernières technologies</li>
                <li><strong>Qualité :</strong> Code propre, testé et documenté</li>
                <li><strong>Collaboration :</strong> Travail d'équipe et communication efficace</li>
                <li><strong>Apprentissage continu :</strong> Formation permanente et veille technologique</li>
            </ul>"""
        }
    )
    print(f"Section A propos: {'Creee' if created else 'Deja existante'}")
    
    # 3. Créer les technologies
    technologies_data = [
        {'name': 'Python', 'skill_level': 95, 'category': 'backend'},
        {'name': 'Django', 'skill_level': 90, 'category': 'backend'},
        {'name': 'JavaScript', 'skill_level': 88, 'category': 'frontend'},
        {'name': 'React', 'skill_level': 85, 'category': 'frontend'},
        {'name': 'Node.js', 'skill_level': 80, 'category': 'backend'},
        {'name': 'PostgreSQL', 'skill_level': 85, 'category': 'database'},
        {'name': 'MongoDB', 'skill_level': 75, 'category': 'database'},
        {'name': 'Docker', 'skill_level': 90, 'category': 'devops'},
        {'name': 'AWS', 'skill_level': 85, 'category': 'devops'},
        {'name': 'Git', 'skill_level': 95, 'category': 'other'},
        {'name': 'Linux', 'skill_level': 90, 'category': 'other'},
        {'name': 'Redis', 'skill_level': 80, 'category': 'other'},
    ]
    
    for tech_data in technologies_data:
        tech, created = Technology.objects.get_or_create(
            name=tech_data['name'],
            defaults={
                'skill_level': tech_data['skill_level'],
                'category': tech_data['category'],
                'is_featured': tech_data['skill_level'] >= 85
            }
        )
        if created:
            print(f"Technologie creee: {tech.name}")
    
    # 4. Créer des témoignages
    testimonials_data = [
        {
            'client_name': 'Marie RAKOTONIRINA',
            'client_position': 'Directrice Marketing, TechMadagascar',
            'content': 'Donaldo a transformé notre plateforme e-commerce avec une expertise remarquable. Son approche méthodique et sa créativité ont dépassé nos attentes.',
            'rating': 5,
            'is_featured': True
        },
        {
            'client_name': 'Jean RANDRIANARIVELO',
            'client_position': 'CEO, StartupInnovation',
            'content': 'Un développeur exceptionnel qui comprend parfaitement les besoins business. Les solutions qu\'il propose sont toujours innovantes et efficaces.',
            'rating': 5,
            'is_featured': True
        },
        {
            'client_name': 'Sarah ANDRIAMANJATO',
            'client_position': 'Product Manager, DigitalSolutions',
            'content': 'Collaboration parfaite avec Donaldo. Il a livré notre application mobile dans les temps avec une qualité exceptionnelle.',
            'rating': 5,
            'is_featured': False
        }
    ]
    
    for testimonial_data in testimonials_data:
        testimonial, created = Testimonial.objects.get_or_create(
            client_name=testimonial_data['client_name'],
            defaults=testimonial_data
        )
        if created:
            print(f"Temoignage cree: {testimonial.client_name}")
    
    # 5. Créer des articles de blog
    blog_posts_data = [
        {
            'title': 'Les 10 Meilleures Pratiques pour le Développement Django en 2024',
            'slug': 'meilleures-pratiques-django-2024',
            'excerpt': 'Découvrez les meilleures pratiques pour développer des applications Django robustes et performantes.',
            'content': """<h2>Introduction</h2>
            <p>Django reste l'un des frameworks Python les plus populaires pour le développement web. Voici les meilleures pratiques à suivre en 2024.</p>
            
            <h3>1. Structure de Projet</h3>
            <p>Organisez votre projet Django avec une structure claire et modulaire...</p>
            
            <h3>2. Gestion des Modèles</h3>
            <p>Utilisez les migrations de manière efficace et gérez les relations entre modèles...</p>
            
            <h3>3. Sécurité</h3>
            <p>Implémentez les bonnes pratiques de sécurité Django...</p>""",
            'tags': 'Django, Python, Développement Web, Bonnes Pratiques',
            'published': True
        },
        {
            'title': 'Optimisation des Performances avec React et Django',
            'slug': 'optimisation-performances-react-django',
            'excerpt': 'Comment optimiser les performances de votre application full-stack React/Django.',
            'content': """<h2>Introduction</h2>
            <p>L'optimisation des performances est cruciale pour une expérience utilisateur fluide...</p>
            
            <h3>1. Optimisation Frontend</h3>
            <p>Techniques d'optimisation React...</p>
            
            <h3>2. Optimisation Backend</h3>
            <p>Optimisation des requêtes Django...</p>""",
            'tags': 'React, Django, Performance, Optimisation',
            'published': True
        }
    ]
    
    for post_data in blog_posts_data:
        post, created = BlogPost.objects.get_or_create(
            slug=post_data['slug'],
            defaults={
                **post_data,
                'author': personal
            }
        )
        if created:
            print(f"Article de blog cree: {post.title}")
    
    # 6. Créer des projets
    from datetime import date
    
    projects_data = [
        {
            'name': 'Plateforme E-commerce TechMadagascar',
            'description': 'Développement complet d\'une plateforme e-commerce moderne avec Django et React. Gestion des commandes, paiements sécurisés, analytics avancés et interface utilisateur intuitive.',
            'short_description': 'Plateforme e-commerce complète avec gestion des commandes, paiements et analytics.',
            'status': 'completed',
            'live_url': 'https://techmadagascar.com',
            'github_url': 'https://github.com/donaldozoubery/techmadagascar',
            'start_date': date(2023, 1, 1),
            'end_date': date(2023, 6, 30),
            'is_featured': True
        },
        {
            'name': 'Application Mobile de Gestion Financière',
            'description': 'Application mobile cross-platform pour la gestion des finances personnelles. Interface intuitive, synchronisation cloud, et analytics de dépenses.',
            'short_description': 'App mobile intuitive pour suivre ses dépenses et investissements.',
            'status': 'completed',
            'live_url': 'https://play.google.com/store/apps/details?id=com.financeapp',
            'github_url': 'https://github.com/donaldozoubery/finance-app',
            'start_date': date(2023, 7, 1),
            'end_date': date(2023, 12, 31),
            'is_featured': True
        },
        {
            'name': 'Système de Monitoring DevOps',
            'description': 'Plateforme de monitoring et alerting pour infrastructures cloud. Dashboards temps réel, alertes intelligentes et intégration avec les principaux services cloud.',
            'short_description': 'Solution complète de monitoring avec dashboards temps réel.',
            'status': 'in_progress',
            'github_url': 'https://github.com/donaldozoubery/devops-monitoring',
            'start_date': date(2024, 1, 1),
            'is_featured': False
        }
    ]
    
    for project_data in projects_data:
        project, created = Project.objects.get_or_create(
            name=project_data['name'],
            defaults=project_data
        )
        if created:
            print(f"Projet cree: {project.name}")
    
    # 7. Créer les paramètres du site
    site_settings, created = SiteSettings.objects.get_or_create(
        defaults={
            'site_title': 'Donaldo ZOUBERY - Portfolio',
            'site_description': 'Développeur Full-Stack passionné par la création d\'expériences digitales exceptionnelles.',
            'hero_title': 'Développeur Full-Stack & Expert DevOps',
            'hero_subtitle': 'Je crée des expériences digitales exceptionnelles',
            'contact_email': 'contact@donaldozoubery.com',
            'contact_phone': '+261 34 00 000 00',
            'address': 'Antananarivo, Madagascar',
            'github_url': 'https://github.com/donaldozoubery',
            'linkedin_url': 'https://linkedin.com/in/donaldozoubery',
            'twitter_url': 'https://twitter.com/donaldozoubery',
            'cv_file': 'cv/donaldo-zoubery-cv.pdf',
            'is_maintenance_mode': False
        }
    )
    print(f"Parametres du site: {'Crees' if created else 'Deja existants'}")
    
    print("\nDonnees de demonstration creees avec succes!")
    print("Resume:")
    print(f"   - Technologies: {Technology.objects.count()}")
    print(f"   - Temoignages: {Testimonial.objects.count()}")
    print(f"   - Articles de blog: {BlogPost.objects.count()}")
    print(f"   - Projets: {Project.objects.count()}")
    print(f"   - Parametres: {SiteSettings.objects.count()}")

if __name__ == '__main__':
    create_demo_data()
