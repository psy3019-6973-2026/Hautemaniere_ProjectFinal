## Hautemaniere_ProjectFinal

# Odor Pleasantness Prediction from EEG

## Description du projet

Ce projet vise à reproduire et améliorer un pipeline EEG permettant de prédire la *pleasantness* (valence hédonique) des odeurs à partir de modèles de machine learning.

Il est basé sur le projet de Xiao (Brainhack) et s’inscrit dans le cadre du cours **PSY3019 – Traitement des données en neurosciences cognitives**.  
L’objectif principal est de rendre le projet plus reproductible, structuré et compréhensible.

---

## Contributions

Projet basé sur : https://github.com/xiao1992/XW_brainhackproject  

Contributions principales :
- Reproduction complète du pipeline
- Création d’un environnement Conda reproductible
- Restructuration du projet en dossiers clairs
- Modularisation du code
- Automatisation avec Invoke
- Amélioration de la documentation
- Réécriture des résultats en Markdown

---

## Reproduire le projet

```bash
git clone <repo_url>
cd Hautemaniere_ProjectFinal
conda env create -f environment_odor_pleasantness.yml
conda activate odor_pleasantness
invoke run


# TÂCHE 1 – REPRODUCTION ET AMÉLIORATION DU PIPELINE

## Partie 1 – Reproduction du notebook original

Reproduire le notebook original à partir d’un environnement propre afin de valider que le pipeline fonctionne correctement de bout en bout.  
Cette étape permet de s’assurer que le projet initial est fonctionnel, d’identifier les dépendances nécessaires et de bien comprendre chaque étape avant toute modification.

### Étapes

- Charger le notebook original `Odor pleasantness.ipynb`
- Exécuter toutes les cellules dans l’ordre
- Vérifier le bon fonctionnement du pipeline complet
- Identifier les éventuelles erreurs, dépendances manquantes ou incohérences
- Ajouter les données directement dans le repository afin d’éviter un téléchargement externe et garantir une exécution immédiate du projet


## Partie 2 – Création d’un environnement reproductible (.yml)

Mettre en place un environnement reproductible afin de permettre à n’importe quel utilisateur d’exécuter le projet dans les mêmes conditions.

### Étapes

- Créer un fichier d’environnement Conda (`environment.yml`)
- Centraliser toutes les dépendances nécessaires
- S’assurer que le projet peut être exécuté à partir de zéro


## Partie 3 – Restructuration du projet

Transformer un projet basé uniquement sur un notebook en une structure de projet claire et organisée.

### Étapes

- Créer une arborescence de projet claire :
  - `code/` : scripts Python
  - `notebook/` : notebook principal
  - `outputs/` : résultats
  - `data/` : données


## Partie 4 – Automatisation du pipeline

Mettre en place une exécution automatisée du projet afin d’améliorer la reproductibilité et de limiter les manipulations manuelles.  
L’objectif est de pouvoir exécuter l’ensemble du pipeline avec une seule commande.

### Étapes

- Ajouter un fichier `tasks.py` contenant des tâches Invoke :
  - `setup` : installation de l’environnement
  - `run` : exécution automatique du notebook
  - `clean` : suppression des outputs
- Ajouter un fichier `invoke.yaml` pour la configuration
- Mettre à jour `environment.yml` pour inclure `invoke` comme dépendance
- Tester l’exécution complète via une commande unique :
  
  ```bash
  invoke run
