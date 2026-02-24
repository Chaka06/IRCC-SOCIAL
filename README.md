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

## Production

1. **Variables d'environnement** (obligatoires en prod) :
   - `DJANGO_SECRET_KEY` : clé secrète (générer avec `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`)
   - `DJANGO_DEBUG=False`
   - `DJANGO_ALLOWED_HOSTS=votredomaine.com,www.votredomaine.com`
   - `CSRF_TRUSTED_ORIGINS=https://votredomaine.com,https://www.votredomaine.com` (si HTTPS)

2. **Fichiers statiques** :
   ```bash
   python manage.py collectstatic --noinput
   ```
   WhiteNoise sert les statiques en production.

3. **Sites (admin)** : Dans Admin Django → Sites, définir le domaine du site (pour sitemap et emails).

4. **Serveur WSGI** : utiliser Gunicorn (ou équivalent) derrière un reverse proxy (Nginx, Caddy).

Exemple Gunicorn :
```bash
pip install gunicorn
gunicorn imigatus_project.wsgi:application --bind 0.0.0.0:8000
```

## Structure

- `imigatus_project/` : configuration Django (settings, urls, WSGI)
- `main/` : app principale (vues, modèles, formulaires, PDF, sitemap)
- `templates/main/` : templates HTML
- `static/` : CSS, JS, images

## Licence

Projet privé.
