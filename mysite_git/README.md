# 🪵 Sticknation : l'observatoire mondial du bâton

**Sticknation** est une plateforme communautaire et scientifique dédiée à l'inventaire, la notation et l'archivage des meilleurs bâtons trouvés dans la nature. 

## Concept et inspiration
Le projet est directement inspiré du phénomène viral **Official Stick Reviews** ([Instagram](https://www.instagram.com/officialstickreviews/) / [Site Web](https://officialstickreviews.com/)). 

L'idée est de reprendre les codes du "sérieux absurde" : traiter un objet simple avec la rigueur d'un expert forestier ou d'un conservateur de musée. Tout le monde a déjà trouvé un bâton "parfait" ; **Sticknation** permet d'officialiser ces découvertes. Chaque spécimen est analysé selon :
- **Handling score (prise en main)** : ergonomie, équilibre, capacité à servir de canne ou d'épée.
- **Aesthetics score (esthétique)** : courbure, texture, patine et prestance visuelle.
- **Géolocalisation** : chaque bâton est répertorié sur une carte mondiale interactive.

---

## Fonctionnalités réalisées (étapes du projet)

Le projet a été transformé d'un blog standard en une application interactive sophistiquée :

### Exploration cartographique (Leaflet et AJAX)
- **Dashboard immersif** : une interface de carte plein écran avec barre latérale rétractable.
- **Multi-fonds de carte** : choix entre vue plan, satellite (Esri) et mode sombre.
- **Voyage temporel** : un slider dynamique (via API JSON interne) permet de filtrer les découvertes par année en temps réel.
- **Mode cumulatif** : visualisation de l'historique de la propagation des trouvailles.
- **Exploration par zones** : chargement dynamique de fichiers **GeoJSON** pour zoomer sur des régions spécifiques.

### Interaction et social
- **Système de "likes" (AJAX)** : approbation des spécimens (❤️) avec mise à jour asynchrone du compteur.
- **Profils experts** : chaque membre possède sa fiche récapitulant l'ensemble de ses "répertoriages".
- **Commentaires hybrides** : système de commentaires intelligent gérant les comptes utilisateurs (login automatique) et les contributions "invité".

### Architecture technique
- **Django 6.0** : utilisation du framework pour la gestion des modèles, des vues et de la sécurité.
- **Base de données relationnelle** : gestion des auteurs, des commentaires, des likes et des fichiers GeoJSON.
- **Gestion des médias** : upload et stockage des photographies de bâtons.

---

## Accès administrateur
Pour tester l'ajout de spécimens, la gestion des zones GeoJSON ou la modération :
- **Utilisateur** : `lucas`
- **Mot de passe** : `lucas`

---

## Installation et lancement

1. **Installer les dépendances** :
   ```bash
   pip install -r requirements.txt

2. **Appliquer les migrations** :
   ```bash
   python manage.py migrate
3. **Lancer le serveur de développement** :
    ```bash
    python manage.py runserver
4. **Accès au site :** :
Ouvrez votre navigateur sur http://127.0.0.1:8000/. Le site redirige automatiquement vers l'application MyBlog/.

Projet réalisé dans le cadre du cours ADYC - 2026 - M2 G2M
