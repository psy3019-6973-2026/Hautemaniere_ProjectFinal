import os
from scipy.io import loadmat


def load_eeg_data(data_root="Hautemaniere_ProjectFinal/Data"):
    """
    Load EEG data organized as:
    subject / condition / odor (.mat files)
    """

    all_data = {}

    for subject_num in range(1, 6):
        subject_name = f"Subject_{subject_num}"
        all_data[subject_name] = {'eyes_open': {}, 'eyes_closed': {}}

        for condition in ['eyes_open', 'eyes_closed']:
            file_prefix = 'O' if condition == 'eyes_open' else 'C'

            for odor_num in range(1, 5):
                file_path = os.path.join(
                    data_root,
                    subject_name,
                    condition,
                    f"{file_prefix}_{odor_num}.mat"
                )

                if os.path.exists(file_path):
                    try:
                        mat = loadmat(file_path)

                        all_data[subject_name][condition][f'odor_{odor_num}'] = {
                            'baseline': mat.get('baseline'),
                            'X_event': mat.get('X_event')
                        }

                    except Exception as e:
                        print(f"Error loading {file_path}: {e}")

    return all_data