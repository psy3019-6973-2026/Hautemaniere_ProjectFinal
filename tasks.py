from pathlib import Path
from invoke import task
import shutil

@task
def setup(c):
    """Install project dependencies."""
    env_file = "environment_odor_pleasantness.yml"

    if Path(env_file).exists():
        print(f"Using {env_file} to update/create the environment...")
        c.run(f"conda env update -f {env_file}", warn=True)
        print("Environment setup complete.")
    else:
        print(f"Error: {env_file} not found.")

@task
def run(c):
    """Execute the main notebook."""
    notebook_path = Path("notebook") / "Odor pleasantness V2.ipynb"

    if not notebook_path.exists():
        print(f"Error: notebook not found at {notebook_path}")
        return

    print(f"Running notebook: {notebook_path}")
    c.run(
        f'jupyter nbconvert --to notebook --execute "{notebook_path}" --output "Odor pleasantness V2.ipynb"',
        warn=True
    )
    print("Notebook execution complete.")

@task
def clean(c):
    """Remove generated outputs."""
    output_dir = Path("outputs")

    if not output_dir.exists():
        print("No outputs folder found. Nothing to clean.")
        return

    shutil.rmtree(output_dir)
    print("Outputs folder removed.")

@task
def status(c):
    """Display project status."""
    paths = {
        "Data": Path("Data"),
        "Code": Path("code"),
        "Notebook": Path("notebook"),
        "Outputs": Path("outputs"),
        "Environment file": Path("environment_odor_pleasantness.yml"),
        "Invoke config": Path("invoke.yaml"),
    }

    print("\nProject status:")
    for name, path in paths.items():
        print(f"- {name}: {'OK' if path.exists() else 'Missing'} ({path})")