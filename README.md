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

## Pourquoi ce projet 

J’ai choisi ce projet parce qu’il me paraissait vraiment intéressant et différent de ce que j’ai déjà fait. Je n’ai jamais travaillé avec des données EEG, donc je trouvais ça motivant de découvrir ce type de données et d’apprendre comment on les analyse. Je trouve aussi très interessant d'essayer de prédire une perception subjective à partir d’un signal cérébral.

## Tâche 1 – Reproduction

Reproduire un notebook existant à partir d’un environnement vierge et documenter le processus.

Avant de modifier ou d’améliorer quoi que ce soit, il est important de comprendre précisément comment fonctionne chaque étape du pipeline. Cela permet également d’identifier les dépendances logicielles, les configurations requises et les éventuels bugs ou zones ambiguës dans le code.

### Étapes

- Installer l’environnement Python requis  
- Charger le notebook `Odor pleasantness.ipynb`  
- Exécuter chaque cellule du notebook dans l’ordre afin de vérifier que le pipeline fonctionne de bout en bout  
- Vérifier que les étapes de prétraitement EEG, d’extraction des features, d’entraînement et de validation se déroulent sans erreur  



## Tâche 2 – Documentation et visualisation

Profiter d’avoir parcouru tout le notebook pour le documenter et retravailler le code afin de le rendre plus lisible.

Après avoir exécuté et compris l’ensemble du notebook, celui-ci sera retravaillé pour être plus clair, mieux structuré et plus facile à réutiliser. Une bonne documentation est essentielle pour assurer la reproductibilité du projet.

### Étapes

- Ajouter une structure claire au notebook (titres par section)
- Créer un fichier `requirements.txt`
- Documenter le code :
  - ajouter des commentaires courts mais informatifs  
  - expliquer la logique des étapes importantes (ce qui est fait et pourquoi)  
- Refactoriser certaines cellules si nécessaire :
  - éviter les répétitions  
  - regrouper certaines étapes en fonctions simples  
  - clarifier les noms de variables



## Tâche 3 – Analyse

Réaliser une analyse exploratoire des données afin de mieux comprendre la structure des données EEG et la variable cible **pleasantness** avant d’interpréter les résultats du modèle.

Cette étape permet d’examiner la distribution des variables, leur variabilité et leurs relations, et d’identifier d’éventuels déséquilibres ou redondances pouvant influencer la performance du modèle.

### Étapes

- Calculer les statistiques descriptives de la variable **pleasantness** (moyenne, écart-type, minimum, maximum)  
- Visualiser la distribution des scores de **pleasantness** à l’aide d’un histogramme  
- Examiner les statistiques descriptives des features EEG extraites (moyenne, variance, dispersion)  
- Calculer et visualiser la matrice de corrélation entre les features EEG afin d’identifier d’éventuelles redondances  
- Analyser la corrélation entre les features EEG et la variable **pleasantness** afin d’identifier les variables potentiellement informatives  



## Tâche bonus – Automatisation 



### Source 
Kroupi, E., Yazdani, A., Vesin, J.M., & Ebrahimi, T. (2014). EEG correlates of pleasant and unpleasant odor perception. ACM Transactions on Multimedia Computing, Communications, and Applications (TOMM), 11(1s), 1–17. [DOI: 10.1145/2637287] 
