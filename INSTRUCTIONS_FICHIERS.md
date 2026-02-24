# 📁 Instructions pour les Fichiers - IRCC

## 🎥 Vidéos Publicitaires

### Dossier : `static/videos/`
Placez vos vidéos dans ce dossier avec ces noms EXACTS :

- **`video1.mp4`** - Première vidéo publicitaire
- **`video2.mp4`** - Deuxième vidéo publicitaire

### Format recommandé :
- **Format** : MP4
- **Résolution** : 720p ou 1080p
- **Durée** : 30-60 secondes maximum
- **Taille** : Moins de 10MB par vidéo

### Comportement :
1. **3 secondes** après le chargement de la page → `video1.mp4` s'affiche
2. Quand `video1.mp4` se termine → **3 secondes d'attente**
3. Puis `video2.mp4` s'affiche automatiquement
4. L'utilisateur peut fermer avec la croix ou la touche Échap

---

## 🖼️ Logo de l'Entreprise

### Dossier : `static/images/`
Placez votre logo avec ce nom EXACT :

- **`logo.png`** - Logo principal de l'entreprise

### Format recommandé :
- **Format** : PNG (avec transparence) ou JPG
- **Résolution** : 200x60 pixels minimum
- **Taille** : Moins de 2MB
- **Couleur** : Compatible avec le thème rouge/blanc canadien

### Utilisation :
- S'affiche dans le header en haut à gauche
- Si le logo n'existe pas, une icône feuille d'érable s'affiche à la place

---

## 📸 Images pour la Procédure

### Dossier : `static/images/`
Placez vos images avec ces noms EXACTS :

- **`procedure1.jpg`** - Image avant "Opportunité d'Emploi au Canada – Informations requises"
- **`procedure2.jpg`** - Image après "Opportunités d'emploi au Canada"

### Format recommandé :
- **Format** : JPG ou PNG
- **Résolution** : 800x600 pixels minimum
- **Taille** : Moins de 5MB par image
- **Contenu** : Images liées à l'immigration canadienne, emploi, ou bureau officiel

---

## 📄 Logo pour les PDF

### Dossier : `media/logos/`
Placez votre logo pour les documents PDF :

- **`logo_entreprise.png`** - Logo pour les documents PDF

### Configuration via l'admin :
1. Allez sur http://localhost:8001/admin/
2. Connectez-vous avec : admin / admin123
3. Allez dans "Informations de l'entreprise"
4. Uploadez votre logo dans le champ "Logo"
5. Sauvegardez

---

## 📱 Numéro WhatsApp

### Configuration via l'admin :
1. Allez sur http://localhost:8001/admin/
2. Connectez-vous avec : admin / admin123
3. Allez dans "Informations de l'entreprise"
4. Remplissez le champ "Numéro WhatsApp" avec : +1234567890
5. Sauvegardez

---

## 🗂️ Structure Complète des Dossiers

```
IMIGATUS/
├── static/
│   ├── videos/
│   │   ├── video1.mp4          ← Première vidéo
│   │   └── video2.mp4          ← Deuxième vidéo
│   └── images/
│       ├── logo.png            ← Logo header
│       ├── procedure1.jpg      ← Image procédure 1
│       └── procedure2.jpg      ← Image procédure 2
├── media/
│   └── logos/
│       └── logo_entreprise.png ← Logo PDF (via admin)
└── ...
```

---

## ✅ Checklist de Vérification

- [ ] `static/videos/video1.mp4` ajouté
- [ ] `static/videos/video2.mp4` ajouté
- [ ] `static/images/logo.png` ajouté
- [ ] `static/images/procedure1.jpg` ajouté
- [ ] `static/images/procedure2.jpg` ajouté
- [ ] Logo uploadé via l'admin Django
- [ ] Numéro WhatsApp configuré via l'admin
- [ ] Test des vidéos sur la page d'accueil
- [ ] Test du logo dans le header
- [ ] Test de la génération PDF avec logo

---

## 🚨 Important

1. **Noms de fichiers EXACTS** - Respectez les noms exacts indiqués
2. **Formats recommandés** - Utilisez les formats suggérés pour de meilleures performances
3. **Tailles optimisées** - Gardez les fichiers légers pour un chargement rapide
4. **Test après ajout** - Vérifiez que tout fonctionne après avoir ajouté les fichiers

---

**IRCC - Immigration, Réfugiés et Citoyenneté Canada** 🇨🇦

