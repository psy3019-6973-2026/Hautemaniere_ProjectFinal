"""
visualization.py - Visualisations pour l'analyse EEG

Ce module crée les figures et visualisations principales.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import plotly.graph_objects as go


def plot_band_diffs(band_diffs, title="Band Power Differences"):
    """
    Plot power difference across channels for each frequency band.
    
    Parameters:
        band_diffs (dict): Band names mapped to difference arrays per channel
        title (str): Title for the plot
    """
    plt.figure(figsize=(10, 4))
    for band, diff in band_diffs.items():
        plt.plot(diff, label=band)
    
    plt.title(f'Band Power Difference (Best - Worst): {title}')
    plt.xlabel('Channel Index')
    plt.ylabel('Power Difference')
    plt.legend()
    plt.tight_layout()
    plt.show()


def plot_feature_importance(top_features, title="Top 20 EEG Features"):
    """
    Plot the top important features from the ML model.
    
    Parameters:
        top_features (DataFrame): DataFrame with columns 'Feature' and 'Importance'
        title (str): Title for the plot
    """
    plt.figure(figsize=(10, 6))
    sns.barplot(data=top_features, x="Importance", y="Feature", palette="viridis")
    plt.title(title)
    plt.tight_layout()
    plt.show()


def plot_model_accuracy(results_df):
    """
    Plot model accuracy comparison across conditions and label types.
    
    Parameters:
        results_df (DataFrame): Results from decode_multiple_models()
    """
    pivot_df = results_df.pivot_table(
        index=['condition', 'label_type'],
        columns='model',
        values='accuracy'
    )
    
    fig, ax = plt.subplots(figsize=(12, 6))
    pivot_df.plot(kind='bar', ax=ax)
    plt.title('Model Accuracy Comparison')
    plt.xlabel('Condition - Label Type')
    plt.ylabel('Accuracy (5-Fold CV)')
    plt.legend(title='Model', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show()


def get_channel_positions(info):
    """
    Extract 3D coordinates and labels for all EEG channels from MNE info.
    
    Parameters:
        info (mne.Info): MNE Info object containing channel information
    
    Returns:
        tuple: (xyz coordinates array, channel labels list)
    """
    xyz = np.array([ch['loc'][:3] for ch in info['chs']])
    labels = [ch['ch_name'] for ch in info['chs']]
    return xyz, labels


def plot_3d_scalp_map(values, info, title="3D Scalp Map"):
    """
    Create interactive 3D scalp map using Plotly.
    
    Parameters:
        values (ndarray): Values to plot on channels (e.g., t-statistics, power differences)
        info (mne.Info): MNE Info object with channel positions
        title (str): Title for the plot
    """
    xyz, labels = get_channel_positions(info)
    
    fig = go.Figure(data=[
        go.Scatter3d(
            x=xyz[:, 0], y=xyz[:, 1], z=xyz[:, 2],
            mode='markers+text',
            marker=dict(
                size=6,
                color=values,
                colorscale='RdBu',
                colorbar=dict(title='T-value'),
                showscale=True,
                opacity=0.9
            ),
            text=labels,
            hoverinfo='text'
        )
    ])
    
    fig.update_layout(
        scene=dict(
            xaxis=dict(visible=False),
            yaxis=dict(visible=False),
            zaxis=dict(visible=False),
            aspectmode='data'
        ),
        title=title,
        margin=dict(l=0, r=0, t=40, b=0)
    )
    fig.show()


def plot_topomaps_group(all_band_maps, info, conditions=['eyes_open', 'eyes_closed'],
                        bands=['theta', 'alpha', 'beta', 'gamma'], 
                        vlim_fixed=0.03, title="Group-Level EEG Band Differences"):
    """
    Create topographical maps for group-level analysis.
    
    Parameters:
        all_band_maps (dict): Dictionary with condition -> band -> power differences
        info (mne.Info): MNE Info object
        conditions (list): Conditions to plot
        bands (list): Frequency bands to plot
        vlim_fixed (float): Voltage limit for color scale
        title (str): Title for the figure
    """
    try:
        from mne.viz import plot_topomap
    except ImportError:
        print("⚠️  MNE not available for topomaps. Skipping visualization.")
        return
    
    fig, axes = plt.subplots(len(conditions), len(bands), figsize=(16, 6))
    
    for row_idx, cond in enumerate(conditions):
        for col_idx, band in enumerate(bands):
            ax = axes[row_idx, col_idx]
            data = all_band_maps[cond][band]

            im, _ = plot_topomap(
                data,
                pos=info,
                axes=ax,
                show=False,
                cmap='RdBu_r',
                vlim=(-vlim_fixed, vlim_fixed),
                contours=6,
                sphere=0.07,
            )

            if row_idx == 0:
                ax.set_title(f'{band.capitalize()} band', fontsize=12)
            if col_idx == 0:
                ax.set_ylabel('Eyes Open' if cond == 'eyes_open' else 'Eyes Closed', fontsize=12)

    fig.subplots_adjust(right=0.92)
    cbar_ax = fig.add_axes([0.94, 0.25, 0.015, 0.5])
    cbar = fig.colorbar(im, cax=cbar_ax)
    cbar.set_label('Power Difference (Best - Worst)', fontsize=12)

    fig.suptitle(title, fontsize=15)
    plt.tight_layout(rect=[0, 0.03, 0.93, 0.95])
    plt.show()
