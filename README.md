# IMIGATUS / IRCC-SOCIAL

Application web d'accompagnement à l'immigration au Canada : candidatures en ligne, vérification passeport/visa, génération PDF, contact WhatsApp.

## Stack

- **Django 5.2** (Python 3.x)
- **Bootstrap 5**, Font Awesome
- **Pillow** (images), **ReportLab** (PDF)

## Installation locale

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env      # optionnel : variables d'environnement
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Ouvrir http://127.0.0.1:8000/

## Déploiement sur PythonAnywhere (gratuit)

Le projet utilise **SQLite** par défaut : pas de base à créer, tout est prêt pour PythonAnywhere.

### 1. Compte et projet

- Crée un compte sur [pythonanywhere.com](https://www.pythonanywhere.com) (plan gratuit).
- Onglet **Web** → **Add a new web app** → **Manual configuration** → **Python 3.10** (ou la version proposée).

### 2. Envoyer le code

- **Option A** : Cloner depuis GitHub  
  Dans l’onglet **Consoles** → ouvre un **Bash**, puis :
  ```bash
  cd ~
  git clone https://github.com/Chaka06/IRCC-SOCIAL.git
  cd IRCC-SOCIAL
  ```
- **Option B** : Upload des fichiers (zip du projet puis extraction dans ton répertoire utilisateur).

### 3. Virtualenv et dépendances

Dans le même Bash :

```bash
cd ~/IRCC-SOCIAL
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Dans l’onglet **Web** → section **Virtualenv**, indique : `/home/TON_USERNAME/IRCC-SOCIAL/venv` (remplace `TON_USERNAME` par ton identifiant PythonAnywhere).

### 4. Variables d’environnement (optionnel)

Dans **Web** → **Code** → **WSGI configuration file**, en haut (avant tout le reste), tu peux définir :

```python
import os
os.environ['DJANGO_ALLOWED_HOSTS'] = 'TON_USERNAME.pythonanywhere.com'
os.environ['DJANGO_DEBUG'] = 'False'
```

Ou laisser les valeurs par défaut du projet (voir `settings.py`).

### 5. Fichier WSGI

Dans **Web** → **Code** → **WSGI configuration file**, remplace le contenu par (en adaptant `TON_USERNAME` et le chemin du projet) :

```python
import os
import sys

path = '/home/TON_USERNAME/IRCC-SOCIAL'
if path not in sys.path:
    sys.path.insert(0, path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'imigatus_project.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

### 6. Migrations et superutilisateur

Dans **Consoles** → **$ Bash** :

```bash
cd ~/IRCC-SOCIAL
source venv/bin/activate
python manage.py migrate
python manage.py createsuperuser
```

### 7. Fichiers statiques

Dans le Bash :

```bash
python manage.py collectstatic --noinput
```

Dans **Web** → **Static files** :
- **URL** : `/static/`
- **Directory** : `/home/TON_USERNAME/IRCC-SOCIAL/staticfiles`

### 8. Redémarrer l’app

Dans **Web** → bouton vert **Reload** pour recharger l’application.

Ton site sera accessible à : **https://TON_USERNAME.pythonanywhere.com**

---

## Production (autres hébergeurs)

Variables utiles : `DJANGO_SECRET_KEY`, `DJANGO_DEBUG=False`, `DJANGO_ALLOWED_HOSTS=ton-domaine.com`. Fichiers statiques : `python manage.py collectstatic`. Optionnel : base PostgreSQL via `DATABASE_URL` (hébergeur externe).

## Structure

- `imigatus_project/` : configuration Django (settings, urls, WSGI)
- `main/` : app principale (vues, modèles, formulaires, PDF, sitemap)
- `templates/main/` : templates HTML
- `static/` : CSS, JS, images

## Licence

Projet privé.
