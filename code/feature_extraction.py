"""
feature_extraction.py - Extraction des features PSD et autres

Ce module extrait les Power Spectral Density (PSD) features
pour chaque bande de fréquence EEG.
"""

import numpy as np
import pandas as pd
from scipy.signal import welch


def extract_psd_features(X, sfreq=250, eeg_bands=None):
    """
    Extract power spectral density (PSD) features for each EEG frequency band.
    
    Parameters:
        X (ndarray): EEG data (time_samples x channels x trials)
        sfreq (float): Sampling frequency in Hz (default: 250)
        eeg_bands (dict): Frequency bands dictionary
    
    Returns:
        ndarray: PSD features (trials x channels*bands)
    """
    if eeg_bands is None:
        eeg_bands = {
            'theta': (4, 7),
            'alpha': (8, 13),
            'beta': (14, 29),
            'gamma': (30, 47)
        }
    
    n_channels = X.shape[1]
    features = []
    
    for trial in range(X.shape[2]):
        trial_data = X[:, :, trial]  
        psd_feats = []
        
        for ch in range(n_channels):
            freqs, psd = welch(trial_data[:, ch], sfreq, nperseg=128)
            
            for band in eeg_bands.values():
                band_power = np.mean(psd[(freqs >= band[0]) & (freqs <= band[1])])
                psd_feats.append(band_power)
        
        features.append(psd_feats)
    
    return np.array(features)


def compute_band_power(X, sfreq=250, eeg_bands=None):
    """
    Compute power in each EEG frequency band for all channels and trials.
    
    Parameters:
        X (ndarray): EEG data (time_samples x channels x trials)
        sfreq (float): Sampling frequency in Hz (default: 250)
        eeg_bands (dict): Frequency bands dictionary
    
    Returns:
        dict: Band names mapped to power arrays (channels x trials)
    """
    if eeg_bands is None:
        eeg_bands = {
            'theta': (4, 7),
            'alpha': (8, 13),
            'beta': (14, 29),
            'gamma': (30, 47)
        }
    
    n_channels = X.shape[1]
    n_trials = X.shape[2]
    band_powers = {band: np.zeros((n_channels, n_trials)) for band in eeg_bands}

    for i in range(n_trials):
        for ch in range(n_channels):
            f, psd = welch(X[:, ch, i], sfreq, nperseg=128)
            
            for band, (low, high) in eeg_bands.items():
                band_mask = (f >= low) & (f <= high)
                band_powers[band][ch, i] = np.mean(psd[band_mask])
    
    return band_powers


def average_band_diff(X_best, X_worst, sfreq=250, eeg_bands=None):
    """
    Compute difference in band power between best and worst odor trials.
    
    Parameters:
        X_best (ndarray): EEG data for pleasant odors (time x channels x trials)
        X_worst (ndarray): EEG data for unpleasant odors (time x channels x trials)
        sfreq (float): Sampling frequency in Hz
        eeg_bands (dict): Frequency bands dictionary
    
    Returns:
        dict: Band names mapped to difference arrays per channel
    """
    power_best = compute_band_power(X_best, sfreq, eeg_bands)
    power_worst = compute_band_power(X_worst, sfreq, eeg_bands)

    band_diffs = {}
    for band in power_best.keys():
        mean_best = np.mean(power_best[band], axis=1)
        mean_worst = np.mean(power_worst[band], axis=1)
        band_diffs[band] = mean_best - mean_worst
    
    return band_diffs


def build_feature_dataframe(eeg_cleaned_dataset, best_worst_map, objective_valence, 
                            eeg_bands=None):
    """
    Build feature matrix from preprocessed EEG with both subjective and objective labels.
    
    Parameters:
        eeg_cleaned_dataset (dict): Preprocessed EEG data
        best_worst_map (dict): Subject ratings
        objective_valence (dict): Objective odor labels
        eeg_bands (dict): Frequency bands
    
    Returns:
        DataFrame: Rows with features, subject, condition, odor, and labels
    """
    if eeg_bands is None:
        eeg_bands = {
            'theta': (4, 7),
            'alpha': (8, 13),
            'beta': (14, 29),
            'gamma': (30, 47)
        }
    
    rows = []
    
    for subject in eeg_cleaned_dataset:
        for condition in ['eyes_open', 'eyes_closed']:
            for odor_key in eeg_cleaned_dataset[subject][condition]:
                odor_num = int(odor_key.split('_')[1])
                X_clean = eeg_cleaned_dataset[subject][condition][odor_key]
                
                if X_clean is None or X_clean.shape[-1] == 0:
                    continue

                feats = extract_psd_features(X_clean, sfreq=250, eeg_bands=eeg_bands)

                for i in range(feats.shape[0]):
                    y_subj = None
                    y_obj = objective_valence.get(odor_num)

                    subj_map = best_worst_map.get(subject, {}).get(condition, {})
                    if subj_map.get('best') == odor_num:
                        y_subj = 1
                    elif subj_map.get('worst') == odor_num:
                        y_subj = 0

                    rows.append({
                        'subject': subject,
                        'condition': condition,
                        'odor': odor_num,
                        'y_subjective': y_subj,
                        'y_objective': y_obj,
                        'features': feats[i]
                    })

    return pd.DataFrame(rows)
