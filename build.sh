#!/usr/bin/env bash
# Script de build pour Render
# Ce script s'exécute automatiquement lors du déploiement

echo "🚀 Démarrage du processus de build..."

# Mise à jour de pip
echo "📦 Mise à jour de pip..."
pip install --upgrade pip

# Installation des dépendances système pour Pillow
echo "🔧 Installation des dépendances système..."
apt-get update
apt-get install -y libjpeg-dev zlib1g-dev libpng-dev

# Installation des dépendances Python
echo "📦 Installation des dépendances Python..."
pip install -r requirements-render.txt

# Collecte des fichiers statiques
echo "📁 Collecte des fichiers statiques..."
python manage.py collectstatic --noinput

# Exécution des migrations
echo "🗄️ Exécution des migrations de base de données..."
python manage.py migrate

# Création d'un superutilisateur par défaut (optionnel)
echo "👤 Création d'un superutilisateur par défaut..."
python manage.py shell << EOF
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print('Superutilisateur créé: admin/admin123')
else:
    print('Superutilisateur existe déjà')
EOF

# Création de données de démonstration
echo "🎨 Création de données de démonstration..."
python data_demo.py

echo "✅ Build terminé avec succès!"
