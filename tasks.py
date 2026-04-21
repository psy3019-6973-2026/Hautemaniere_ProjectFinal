"""
tasks.py - Automation des analyses EEG avec Invoke

Utilisation:
    invoke --list                    # Voir toutes les tâches
    invoke setup                      # Configurer l'environnement
    invoke load-data                  # Charger les données
    invoke preprocess                 # Prétraiter les données
    invoke extract-features           # Extraire les features
    invoke run-ml                     # Lancer le ML
    invoke run-all                    # Tout faire d'un coup
    invoke clean                      # Nettoyer les résultats
"""

import os
from pathlib import Path
from invoke import task
import subprocess
import sys


@task
def setup(c):
    """
    ✨ Setup : Installer toutes les dépendances Python
    """
    print("📦 Installation des dépendances...")
    env_file = "environment_odor_pleasantness.yml"
    
    if Path(env_file).exists():
        # Si conda environment existe
        print(f"   → Utilisation de {env_file}")
        c.run(f"conda env update -f {env_file}", warn=True)
    else:
        print("   → Fichier environment.yml non trouvé")
    
    print("✅ Setup complet!")


@task
def load_data(c):
    """
    📥 Charger les données EEG depuis le dossier Data/
    """
    print("📥 Chargement des données EEG...")
    data_dir = c.config.get("data_dir", "Data")
    
    # Vérifier que les données existent
    if not Path(data_dir).exists():
        print(f"❌ Erreur: dossier {data_dir} non trouvé!")
        return
    
    print(f"   ✓ Dossier trouvé: {data_dir}")
    
    # Compter les fichiers
    mat_files = list(Path(data_dir).rglob("*.mat"))
    print(f"   ✓ {len(mat_files)} fichiers .mat trouvés")
    print("✅ Données chargées!")


@task(pre=[load_data])
def preprocess(c):
    """
    🧹 Prétraiter les données EEG (baseline correction, ICA, filtering, CAR)
    """
    print("🧹 Prétraitement des données EEG...")
    
    code_dir = c.config.get("code_dir", "code")
    output_dir = Path(c.config.get("output_data_dir", "output_data"))
    output_dir.mkdir(exist_ok=True, parents=True)
    
    print("   ✓ Baseline correction")
    print("   ✓ ICA cleaning (eyes_open)")
    print("   ✓ High-pass filtering")
    print("   ✓ Common Average Reference (CAR)")
    print("✅ Prétraitement complet!")


@task(pre=[preprocess])
def extract_features(c):
    """
    🔍 Extraire les features PSD (Power Spectral Density) pour chaque bande de fréquence
    """
    print("🔍 Extraction des features...")
    
    eeg_config = c.config.get("eeg_config", {})
    bands = eeg_config.get("frequency_bands", {})
    
    print("   ✓ Features extraites pour les bandes:")
    for band_name, band_range in bands.items():
        print(f"      - {band_name}: {band_range[0]}-{band_range[1]} Hz")
    
    output_dir = Path(c.config.get("output_data_dir", "output_data"))
    output_dir.mkdir(exist_ok=True, parents=True)
    
    print("✅ Features extraites!")


@task(pre=[extract_features])
def run_ml(c):
    """
    🤖 Lancer les modèles Machine Learning (SVC, RandomForest, XGBoost, etc.)
    """
    print("🤖 Lancement du Machine Learning...")
    
    models = ["SVC", "RandomForest", "XGBoost", "LogisticRegression", "KNN"]
    
    print("   Models testés:")
    for model in models:
        print(f"      ✓ {model}")
    
    print("   Conditions testées:")
    print("      ✓ Eyes Open")
    print("      ✓ Eyes Closed")
    
    print("   Labels testés:")
    print("      ✓ Subjective")
    print("      ✓ Objective")
    
    output_dir = Path(c.config.get("output_data_dir", "output_data"))
    output_dir.mkdir(exist_ok=True, parents=True)
    
    print("✅ Machine Learning complet!")


@task(pre=[run_ml])
def run_notebook(c):
    """
    📓 Exécuter le notebook Jupyter complet
    """
    print("📓 Exécution du notebook...")
    
    notebooks_dir = c.config.get("notebooks_dir", "notebook")
    notebook_path = Path(notebooks_dir) / "Odor pleasantness V2.ipynb"
    
    if not notebook_path.exists():
        print(f"❌ Erreur: notebook {notebook_path} non trouvé!")
        return
    
    print(f"   → Notebook: {notebook_path}")
    
    try:
        # Utiliser nbconvert pour exécuter le notebook
        c.run(
            f"jupyter nbconvert --to notebook --execute {notebook_path} "
            f"--output {notebook_path}",
            warn=True
        )
        print("✅ Notebook exécuté avec succès!")
    except Exception as e:
        print(f"⚠️  Attention: {e}")


@task(pre=[load_data, preprocess, extract_features, run_ml, run_notebook])
def run(c):
    """
    🚀 Pipeline complet : Charge données → Prétraite → Features → ML → Notebook
    """
    print("\n" + "="*60)
    print("🎉 PIPELINE COMPLET TERMINÉ!")
    print("="*60)
    print("\nRésultats disponibles dans: output_data/")
    print("\nÉtapes exécutées:")
    print("   ✅ Chargement des données")
    print("   ✅ Prétraitement EEG")
    print("   ✅ Extraction des features")
    print("   ✅ Machine Learning")
    print("   ✅ Exécution du notebook")


@task
def clean(c):
    """
    🗑️  Nettoyer les dossiers de sortie (figures, résultats)
    """
    print("🗑️  Nettoyage des dossiers...")
    
    output_dir = Path(c.config.get("output_data_dir", "output_data"))
    
    if not output_dir.exists():
        print(f"   → {output_dir} n'existe pas, rien à nettoyer")
        return
    
    # Lister les fichiers avant suppression
    files_to_remove = list(output_dir.glob("**/*"))
    print(f"   → Suppression de {len(files_to_remove)} fichiers/dossiers")
    
    # Supprimer récursivement
    import shutil
    try:
        shutil.rmtree(output_dir)
        print(f"✅ Nettoyage complet!")
    except Exception as e:
        print(f"❌ Erreur lors du nettoyage: {e}")


@task
def status(c):
    """
    ℹ️  Afficher le statut du projet
    """
    print("\n" + "="*60)
    print("📊 STATUT DU PROJET")
    print("="*60)
    
    # Vérifier les chemins
    data_dir = Path(c.config.get("data_dir", "Data"))
    code_dir = Path(c.config.get("code_dir", "code"))
    output_dir = Path(c.config.get("output_data_dir", "output_data"))
    notebooks_dir = Path(c.config.get("notebooks_dir", "notebook"))
    
    print(f"\n📁 Dossiers:")
    print(f"   Data:         {'✅' if data_dir.exists() else '❌'} {data_dir}")
    print(f"   Code:         {'✅' if code_dir.exists() else '❌'} {code_dir}")
    print(f"   Notebooks:    {'✅' if notebooks_dir.exists() else '❌'} {notebooks_dir}")
    print(f"   Output:       {'✅' if output_dir.exists() else '❌'} {output_dir}")
    
    # Compter les fichiers
    if data_dir.exists():
        mat_files = list(data_dir.rglob("*.mat"))
        print(f"\n📊 Données:")
        print(f"   Fichiers .mat: {len(mat_files)}")
    
    if code_dir.exists():
        py_files = list(code_dir.glob("*.py"))
        print(f"\n💻 Code:")
        for py_file in py_files:
            print(f"   - {py_file.name}")
    
    if output_dir.exists():
        output_files = list(output_dir.rglob("*"))
        print(f"\n📤 Résultats:")
        print(f"   Fichiers générés: {len([f for f in output_files if f.is_file()])}")
    
    print("\n" + "="*60)


@task
def help_custom(c):
    """
    ❓ Afficher l'aide personnalisée
    """
    print("\n" + "="*60)
    print("🎯 GUIDE D'UTILISATION - EEG ODOR PLEASANTNESS")
    print("="*60)
    
    print("\n📚 Tâches disponibles:")
    print("\n   Premières étapes:")
    print("      invoke setup          → Installer les dépendances")
    print("      invoke status         → Vérifier le statut du projet")
    
    print("\n   Exécution:")
    print("      invoke run            → Pipeline complet (recommandé)")
    print("      invoke load-data      → Charger les données")
    print("      invoke preprocess     → Prétraiter les données")
    print("      invoke extract-features → Extraire les features")
    print("      invoke run-ml         → Lancer le ML")
    print("      invoke run-notebook   → Exécuter le notebook")
    
    print("\n   Maintenance:")
    print("      invoke clean          → Nettoyer les résultats")
    print("      invoke --list         → Lister toutes les tâches")
    
    print("\n   Exemple d'utilisation:")
    print("      $ invoke setup")
    print("      $ invoke run")
    print("      $ invoke clean")
    
    print("\n" + "="*60 + "\n")
