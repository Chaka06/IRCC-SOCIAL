# 📸 Instructions pour les Images - IRCC

## 🎯 Images Requises

### 🏠 Page d'Accueil
- **Logo** : `static/images/logo.png` (200x60px minimum)
- **Image Hero** : `static/images/hero_image.png` (800x400px)

### 🎥 Vidéos Publicitaires
- **Vidéo 1** : `static/videos/video1.mp4` (30-60 secondes, < 10MB)
- **Vidéo 2** : `static/videos/video2.mp4` (30-60 secondes, < 10MB)

### 📋 Page Procédure
- **Image Hero Procédure** : `static/images/procedure_hero.png` (600x300px)
- **Bannière Opportunité** : `static/images/ad_opportunity.png` (800x200px)
- **Bannière Conditions** : `static/images/ad_conditions.png` (800x200px)

### 👥 Membres de l'Équipe
- **Tremblay Olivia** : `static/images/tremblay_olivia.png` (300x300px, carré)
- **BADAA MOREL** : `static/images/badaa_morel.png` (300x300px, carré)

## 📁 Structure des Dossiers

```
IMIGATUS/
├── static/
│   ├── images/
│   │   ├── logo.png
│   │   ├── hero_image.png
│   │   ├── procedure_hero.png
│   │   ├── ad_opportunity.png
│   │   ├── ad_conditions.png
│   │   ├── tremblay_olivia.png
│   │   └── badaa_morel.png
│   └── videos/
│       ├── video1.mp4
│       └── video2.mp4
```

## 🎨 Spécifications Techniques

### Images
- **Format** : PNG (avec transparence) ou JPG
- **Résolution** : 72 DPI minimum
- **Couleurs** : Respecter la charte graphique IRCC (bleus et rouge)

### Vidéos
- **Format** : MP4 (H.264)
- **Résolution** : 720p minimum
- **Durée** : 30-60 secondes
- **Taille** : < 10MB par vidéo

## 📝 Contenu des Images

### Bannière Opportunité (`ad_opportunity.png`)
- **Titre** : "Opportunité d'Emploi au Canada"
- **Sous-titre** : "Informations requises"
- **Style** : Professionnel, couleurs IRCC

### Bannière Conditions (`ad_conditions.png`)
- **Titre** : "Conditions et Avantages"
- **Sous-titre** : "Frais de passeport temporaire : 367$"
- **Style** : Professionnel, couleurs IRCC

### Membres de l'Équipe
- **Photos professionnelles** en costume
- **Fond neutre** (blanc ou bleu clair)
- **Qualité haute résolution**

## 🚀 Comment Ajouter les Images

### Option 1 : Via Finder (Mac)
1. Ouvrez **Finder**
2. Naviguez vers `/Users/mac.chaka/Desktop/IMIGATUS/static/images/`
3. Glissez vos images avec les noms exacts
4. Répétez pour `/Users/mac.chaka/Desktop/IMIGATUS/static/videos/`

### Option 2 : Via Terminal
```bash
# Copier les images
cp /chemin/vers/votre/logo.png ~/Desktop/IMIGATUS/static/images/
cp /chemin/vers/votre/hero_image.png ~/Desktop/IMIGATUS/static/images/
cp /chemin/vers/votre/procedure_hero.png ~/Desktop/IMIGATUS/static/images/
cp /chemin/vers/votre/ad_opportunity.png ~/Desktop/IMIGATUS/static/images/
cp /chemin/vers/votre/ad_conditions.png ~/Desktop/IMIGATUS/static/images/
cp /chemin/vers/votre/tremblay_olivia.png ~/Desktop/IMIGATUS/static/images/
cp /chemin/vers/votre/badaa_morel.png ~/Desktop/IMIGATUS/static/images/

# Copier les vidéos
cp /chemin/vers/votre/video1.mp4 ~/Desktop/IMIGATUS/static/videos/
cp /chemin/vers/votre/video2.mp4 ~/Desktop/IMIGATUS/static/videos/
```

## ✅ Vérification

Après avoir ajouté les images :
1. **Actualisez** la page : http://localhost:8001
2. **Vérifiez** que toutes les images s'affichent
3. **Testez** les vidéos publicitaires
4. **Vérifiez** la page procédure : http://localhost:8001/procedure/

## 🎨 Charte Graphique IRCC

### Couleurs Principales
- **Bleu sombre** : #1B365D
- **Bleu mat** : #2C5F7C
- **Bleu clair** : #4A90A4
- **Rouge accent** : #D32F2F
- **Blanc** : #FFFFFF

### Typographie
- **Police principale** : Inter, Roboto
- **Style** : Professionnel, gouvernemental
- **Taille** : Lisible sur mobile et desktop

---

**Note** : Toutes les images doivent respecter les droits d'auteur et être libres d'utilisation.

