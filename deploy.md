# 🚀 Guide de Déploiement - Portfolio Ultra-Moderne

## 📋 Prérequis

- Compte GitHub
- Compte Render (gratuit)
- Base de données PostgreSQL
- Variables d'environnement configurées

## 🌐 Déploiement sur Render

### 1. Préparation du Repository

```bash
# Initialiser Git si ce n'est pas déjà fait
git init
git add .
git commit -m "Initial commit - Portfolio ultra-moderne"

# Connecter au repository GitHub
git remote add origin https://github.com/votre-username/portfolio-ultra-moderne.git
git push -u origin main
```

### 2. Configuration sur Render

1. **Se connecter à [Render](https://render.com)**
2. **Créer un nouveau service "Web Service"**
3. **Connecter le repository GitHub**
4. **Configurer les paramètres :**
   - **Name** : `donaldo-portfolio`
   - **Environment** : `Python 3`
   - **Build Command** : `./build.sh`
   - **Start Command** : `gunicorn config.wsgi:application`

### 3. Variables d'Environnement

Configurer les variables suivantes dans Render :

```bash
DEBUG=False
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=donaldo-portfolio.onrender.com
DATABASE_URL=postgresql://username:password@host:port/dbname
CLOUD_NAME=your-cloudinary-name
CLOUD_API_KEY=your-cloudinary-key
CLOUD_API_SECRET=your-cloudinary-secret
EMAIL_HOST_USER=your-email@domain.com
EMAIL_HOST_PASSWORD=your-email-password
RECAPTCHA_PUBLIC_KEY=your-recaptcha-public-key
RECAPTCHA_PRIVATE_KEY=your-recaptcha-private-key
```

### 4. Base de Données PostgreSQL

1. **Créer une base de données PostgreSQL** sur Render
2. **Copier l'URL de connexion** dans `DATABASE_URL`
3. **La base sera automatiquement migrée** lors du déploiement

## 🔧 Configuration Post-Déploiement

### 1. Accès à l'Administration

```bash
# Créer un superutilisateur
python manage.py createsuperuser

# Ou utiliser les données de démonstration
# Login: admin / Password: admin123
```

### 2. Configuration des Données

1. **Accéder à l'admin Django** : `https://votre-app.onrender.com/admin/`
2. **Ajouter vos informations personnelles**
3. **Configurer les technologies**
4. **Ajouter des projets et articles**

## 🚀 Déploiement Automatique

Le déploiement se fait automatiquement à chaque push sur la branche `main` :

```bash
git add .
git commit -m "Update portfolio"
git push origin main
```

## 🔍 Vérification du Déploiement

1. **Vérifier l'URL** : `https://votre-app.onrender.com`
2. **Tester les fonctionnalités** :
   - Navigation
   - Formulaire de contact
   - Portfolio
   - Blog
3. **Vérifier les logs** dans le dashboard Render

## 🛠️ Dépannage

### Erreurs Communes

1. **Erreur de migration** :
   ```bash
   # Vérifier les logs Render
   # Relancer le build si nécessaire
   ```

2. **Fichiers statiques** :
   ```bash
   # Vérifier que collectstatic fonctionne
   python manage.py collectstatic --noinput
   ```

3. **Variables d'environnement** :
   ```bash
   # Vérifier que toutes les variables sont définies
   # Vérifier les noms des variables (sensible à la casse)
   ```

### Logs et Monitoring

- **Logs en temps réel** : Dashboard Render > Logs
- **Métriques** : Dashboard Render > Metrics
- **Base de données** : Dashboard Render > Database

## 📈 Optimisation

### Performance

1. **Activer le cache** (optionnel)
2. **Optimiser les images** avec Cloudinary
3. **Minifier les assets** (déjà fait)

### Sécurité

1. **Configurer HTTPS** (automatique sur Render)
2. **Mettre à jour les dépendances** régulièrement
3. **Sauvegarder la base de données** régulièrement

## 🔄 Mises à Jour

### Processus de Mise à Jour

1. **Modifier le code localement**
2. **Tester en local**
3. **Commit et push** :
   ```bash
   git add .
   git commit -m "Update: description des changements"
   git push origin main
   ```
4. **Vérifier le déploiement** automatique

### Rollback

En cas de problème, vous pouvez revenir à une version précédente :

1. **Dashboard Render** > **Deploys**
2. **Sélectionner une version précédente**
3. **Cliquer sur "Deploy"**

## 📞 Support

En cas de problème :

1. **Vérifier les logs** Render
2. **Consulter la documentation** Django
3. **Créer une issue** sur GitHub
4. **Contacter le support** Render

---

🎉 **Votre portfolio ultra-moderne est maintenant déployé et prêt à épater vos prospects !** 🚀
