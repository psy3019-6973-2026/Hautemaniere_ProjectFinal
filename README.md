## Hautemaniere_ProjectFinal

# PROJET – EEG-Based Odor Preference Modeling

## Présentation du projet

Ce projet vise à prédire le niveau de **pleasantness** (caractère agréable ou désagréable) d’odeurs à partir de données EEG.  
L’objectif est de déterminer si l’activité cérébrale enregistrée pendant l’exposition à différentes odeurs permet d’anticiper les évaluations subjectives données par les participants.
Pour cela, des features sont extraites des signaux EEG puis utilisées pour entraîner un modèle de machine learning capable de prédire les scores de pleasantness. L’objectif est d’évaluer dans quelle mesure ces modèles peuvent établir un lien fiable entre activité cérébrale et perception subjective des odeurs.


## Données

Les données proviennent de la base **OPPD (Odor Pleasantness Perception Database)** développée par Kroupi et al. (2014).

### Participants

Le dataset comprend des enregistrements EEG réalisés chez **cinq participants masculins âgés de 26 à 32 ans**.

### Odeurs présentées

- Valériane 🌿 
- Fleur de lotus 🪷  
- Fromage 🧀
- Eau de rose 🌹

### Conditions expérimentales

Pour chaque sujet, deux conditions ont été testées :

- Yeux ouverts  
- Yeux fermés  

Chaque essai comprend :
- une période de **baseline**
- une période correspondant à la **présentation de l’odeur**

Les signaux EEG ont été enregistrés à l’aide d’un système à **256 électrodes**, avec une fréquence d’échantillonnage de **250 Hz**.



## Variables

Après chaque exposition, les participants ont évalué les odeurs en termes :

- d’intensité  
- de pleasantness  

Dans ce projet :

- les **features EEG extraites** constituent les variables explicatives (**X**)  
- les **scores de pleasantness** constituent la variable cible (**y**) du modèle  



## Pipeline du projet

1. Prétraitement du signal EEG  
2. Extraction des features  
3. Entraînement du modèle  
4. Validation des performances

## Résultats

- Il existe un léger accord entre les évaluations subjectives des participants et les labels objectifs des odeurs, mais le résultat n’est pas statistiquement significatif.
- Les performances sont meilleures lorsque les yeux sont ouverts, ce qui suggère que le contexte visuel influence l’évaluation des odeurs.
- Les modèles de machine learning prédisent mieux la pleasantness objective que les préférences subjectives, qui sont plus variables entre individus.

<img width="576" height="432" alt="image" src="https://raw.githubusercontent.com/xiao1992/XW_brainhackproject/refs/heads/main/figures/ML%20results.png" />

## Pourquoi ce projet 

J’ai choisi ce projet parce qu’il me paraissait vraiment intéressant et différent de ce que j’ai déjà fait. Je n’ai jamais travaillé avec des données EEG, donc je trouvais ça motivant de découvrir ce type de données et d’apprendre comment on les analyse. Je trouve aussi très interessant d'essayer de prédire une perception subjective à partir d’un signal cérébral.


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
