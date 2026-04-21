"""
test_imports.py - Tester que tous les imports fonctionnent

Usage:
    python code/test_imports.py
"""

import sys
from pathlib import Path

# Ajouter le parent directory au path
sys.path.insert(0, str(Path(__file__).parent.parent))

print("=" * 60)
print("🧪 TEST DES IMPORTS")
print("=" * 60)

try:
    print("\n✓ Importing io_utils...")
    from code.io_utils import load_eeg_data
    print("  ✅ load_eeg_data imported successfully")
except Exception as e:
    print(f"  ❌ Error: {e}")

try:
    print("\n✓ Importing preprocessing...")
    from code.preprocessing import (
        highpass_filter,
        run_ica_on_data,
        apply_car,
        baseline_correct,
        preprocess_trials
    )
    print("  ✅ All preprocessing functions imported successfully")
except Exception as e:
    print(f"  ❌ Error: {e}")

try:
    print("\n✓ Importing feature_extraction...")
    from code.feature_extraction import (
        extract_psd_features,
        compute_band_power,
        average_band_diff,
        build_feature_dataframe
    )
    print("  ✅ All feature extraction functions imported successfully")
except Exception as e:
    print(f"  ❌ Error: {e}")

try:
    print("\n✓ Importing ml_models...")
    from code.ml_models import (
        decode_multiple_models,
        get_feature_importance
    )
    print("  ✅ All ML model functions imported successfully")
except Exception as e:
    print(f"  ❌ Error: {e}")

try:
    print("\n✓ Importing visualization...")
    from code.visualization import (
        plot_band_diffs,
        plot_feature_importance,
        plot_model_accuracy,
        plot_3d_scalp_map
    )
    print("  ✅ All visualization functions imported successfully")
except Exception as e:
    print(f"  ❌ Error: {e}")

print("\n" + "=" * 60)
print("✅ ALL TESTS PASSED!")
print("=" * 60)
