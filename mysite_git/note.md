# 📝 note d'accompagnement du projet

**objet :** rendu du projet d'inventaire cartographique sticknation
**auteur :** lucas
**date :** février 2026

## 📌 présentation du projet
ce projet consiste en une plateforme web dynamique d'inventaire de bâtons, inspirée par la tendance "official stick reviews". l'objectif technique était de transformer un système de blog classique en une application cartographique interactive utilisant des flux de données asynchrones (ajax).

## 🚀 points techniques majeurs
le développement s'est concentré sur plusieurs fonctionnalités avancées pour enrichir l'expérience utilisateur :

* **cartographie immersive :** intégration de la librairie leaflet avec gestion de multiples couches (plan, satellite, mode sombre).
* **gestion de données temporelles :** mise en place d'un slider dynamique permettant de filtrer les publications par année sans rechargement de page (via une api json interne).
* **interactions asynchrones (ajax) :** implémentation d'un système de "likes" en temps réel et de chargement dynamique de fichiers geojson pour le découpage géographique.
* **architecture des templates :** mise en place d'un système d'héritage de templates avec un fichier `base.html` structuré pour assurer la cohérence visuelle de l'application.

## 🛠️ environnement de test
pour faciliter la correction, un compte administrateur a été pré-configuré :
* **identifiant :** `lucas`
* **mot de passe :** `lucas`

le projet inclut également un fichier `requirements.txt` listant l'ensemble des dépendances (django, folium, geopy, etc.) nécessaires au bon fonctionnement de l'application.

## ⚠️ remarques complémentaires
le projet a été testé sous environnement windows. en cas de difficulté d'affichage des templates lors du déploiement, la configuration du paramètre `DIRS` dans le fichier `settings.py` a été optimisée pour utiliser des chemins absolus via `os.path.join` afin de garantir une compatibilité maximale.