# 📸 Instructions Complètes pour les Images - IRCC

## 📁 **Emplacements des Images**

### **Dossier Principal**
```
/Users/mac.chaka/Desktop/IMIGATUS/static/images/
```

### **Dossier Vidéos**
```
/Users/mac.chaka/Desktop/IMIGATUS/static/videos/
```

## 🎯 **Images Requises - Liste Complète**

### **🏠 Images Principales**
1. **Logo** : `logo.png` (200x60px minimum)
2. **Image Hero** : `hero_image.png` (800x400px)
3. **Image Procédure** : `procedure_hero.png` (600x300px)

### **📋 Bannières Publicitaires**
4. **Bannière Opportunité** : `ad_opportunity.png` (800x200px)
5. **Bannière Conditions** : `ad_conditions.png` (800x200px)
6. **Immigration Express** : `immigration_express.png` (800x300px)

### **👥 Photos de l'Équipe**
7. **Tremblay Olivia** : `tremblay_olivia.png` (300x300px, carré)
8. **BADAA MOREL** : `badaa_morel.png` (300x300px, carré)

### **📄 Images de Produits (Documents Officiels)**
9. **Passeport Canadien** : `passeport_canadien.png` (400x300px)
10. **Visa de Travail** : `visa_travail.png` (400x300px)
11. **Carte de Résidence** : `carte_residence.png` (400x300px)
12. **Permis de Travail** : `permis_travail.png` (400x300px)

### **🎥 Vidéos**
13. **Vidéo 1** : `video1.mp4` (30-60 secondes, < 10MB)
14. **Vidéo 2** : `video2.mp4` (30-60 secondes, < 10MB)

## 📂 **Structure Complète des Dossiers**

```
IMIGATUS/
├── static/
│   ├── images/
│   │   ├── logo.png                    ← Logo IRCC
│   │   ├── hero_image.png              ← Image hero page d'accueil
│   │   ├── procedure_hero.png          ← Image hero page procédure
│   │   ├── ad_opportunity.png          ← Bannière opportunité emploi
│   │   ├── ad_conditions.png           ← Bannière conditions
│   │   ├── immigration_express.png     ← Bannière immigration express
│   │   ├── tremblay_olivia.png         ← Photo Tremblay Olivia
│   │   ├── badaa_morel.png             ← Photo BADAA MOREL
│   │   ├── passeport_canadien.png      ← Image passeport canadien
│   │   ├── visa_travail.png            ← Image visa de travail
│   │   ├── carte_residence.png         ← Image carte de résidence
│   │   └── permis_travail.png          ← Image permis de travail
│   └── videos/
│       ├── video1.mp4                  ← Première vidéo publicitaire
│       └── video2.mp4                  ← Deuxième vidéo publicitaire
```

## 🎨 **Spécifications Techniques**

### **Images**
- **Format** : PNG (avec transparence) ou JPG
- **Résolution** : 72 DPI minimum
- **Couleurs** : Respecter la charte graphique IRCC (bleus et rouge)
- **Qualité** : Haute résolution pour un rendu professionnel

### **Vidéos**
- **Format** : MP4 (H.264)
- **Résolution** : 720p minimum
- **Durée** : 30-60 secondes
- **Taille** : < 10MB par vidéo

## 📝 **Contenu des Images de Produits**

### **Passeport Canadien** (`passeport_canadien.png`)
- **Contenu** : Image d'un passeport canadien ouvert ou fermé
- **Style** : Professionnel, couleurs officielles
- **Message** : "Passeport Canadien - Délivré en 72h"

### **Visa de Travail** (`visa_travail.png`)
- **Contenu** : Image d'un visa de travail canadien
- **Style** : Document officiel, couleurs gouvernementales
- **Message** : "Visa de Travail - Intégré dans le passeport"

### **Carte de Résidence** (`carte_residence.png`)
- **Contenu** : Image d'une carte de résidence permanente
- **Style** : Document officiel canadien
- **Message** : "Résidence Permanente - Tous les droits canadiens"

### **Permis de Travail** (`permis_travail.png`)
- **Contenu** : Image d'un permis de travail canadien
- **Style** : Document officiel, design gouvernemental
- **Message** : "Permis de Travail - Temporaire ou Permanent"

## 🚀 **Comment Ajouter les Images**

### **Option 1 : Via Finder (Mac)**
1. Ouvrez **Finder**
2. Naviguez vers `/Users/mac.chaka/Desktop/IMIGATUS/static/images/`
3. Glissez toutes vos images avec les noms exacts
4. Répétez pour `/Users/mac.chaka/Desktop/IMIGATUS/static/videos/`

### **Option 2 : Via Terminal**
```bash
# Aller dans le dossier images
cd ~/Desktop/IMIGATUS/static/images/

# Copier toutes les images (remplacez par vos vrais chemins)
cp /chemin/vers/votre/logo.png logo.png
cp /chemin/vers/votre/hero_image.png hero_image.png
cp /chemin/vers/votre/procedure_hero.png procedure_hero.png
cp /chemin/vers/votre/ad_opportunity.png ad_opportunity.png
cp /chemin/vers/votre/ad_conditions.png ad_conditions.png
cp /chemin/vers/votre/immigration_express.png immigration_express.png
cp /chemin/vers/votre/tremblay_olivia.png tremblay_olivia.png
cp /chemin/vers/votre/badaa_morel.png badaa_morel.png
cp /chemin/vers/votre/passeport_canadien.png passeport_canadien.png
cp /chemin/vers/votre/visa_travail.png visa_travail.png
cp /chemin/vers/votre/carte_residence.png carte_residence.png
cp /chemin/vers/votre/permis_travail.png permis_travail.png

# Aller dans le dossier vidéos
cd ../videos/

# Copier les vidéos
cp /chemin/vers/votre/video1.mp4 video1.mp4
cp /chemin/vers/votre/video2.mp4 video2.mp4
```

## ✅ **Vérification**

Après avoir ajouté toutes les images :

1. **Redémarrez le serveur** :
   ```bash
   cd ~/Desktop/IMIGATUS
   python manage.py runserver 8001
   ```

2. **Testez toutes les pages** :
   - **Accueil** : http://localhost:8001
   - **Services** : http://localhost:8001/services/
   - **Procédure** : http://localhost:8001/procedure/
   - **À Propos** : http://localhost:8001/about/
   - **Contact** : http://localhost:8001/contact/

3. **Vérifiez** :
   - ✅ Toutes les images s'affichent
   - ✅ Les vidéos publicitaires fonctionnent
   - ✅ Les bannières de produits sont visibles
   - ✅ Les photos de l'équipe s'affichent

## 🎨 **Charte Graphique IRCC**

### **Couleurs Principales**
- **Bleu sombre** : #1B365D
- **Bleu mat** : #2C5F7C
- **Bleu clair** : #4A90A4
- **Rouge accent** : #D32F2F
- **Blanc** : #FFFFFF

### **Style des Images**
- **Professionnel** : Qualité gouvernementale
- **Cohérent** : Même style sur toutes les images
- **Couleurs** : Respecter la charte IRCC
- **Lisibilité** : Texte clair et lisible

---

**Note** : Toutes les images doivent respecter les droits d'auteur et être libres d'utilisation. Les images de documents officiels doivent être des représentations réalistes mais ne pas être de vrais documents.

