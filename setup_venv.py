# setup_venv.py

import os
import platform
import subprocess
import sys
from typing import Optional


def create_virtualenv(project_name: str) -> None:
    """Create a virtual environment and install dependencies from pyproject.toml if available.

    Args:
        project_name (str): The name of the project for which to create the virtual environment.
    """
    # Define the path for the virtual environment
    home = os.path.expanduser("~")
    venv_path = os.path.join(home, ".virtualenvs", project_name)

    # Create the virtual environment
    try:
        subprocess.check_call([sys.executable, "-m", "venv", venv_path])
        print(f"Virtual environment created at: {venv_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error creating virtual environment: {e}")
        sys.exit(1)

    # Activate the virtual environment based on the OS
    if platform.system() == "Windows":
        activate_script = os.path.join(venv_path, "Scripts", "activate")
    else:
        activate_script = os.path.join(venv_path, "bin", "activate")

    print(
        f"To activate it, run: source {activate_script} (Linux/Mac) or {activate_script} (Windows)"
    )

    # Install packages from pyproject.toml if it exists
    try:
        subprocess.check_call([os.path.join(venv_path, "bin", "pip"), "install", "."])
        print("Dependencies installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error installing dependencies: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python setup_venv.py <project_name>")
        sys.exit(1)

    project_name = sys.argv[1]
    create_virtualenv(project_name)
