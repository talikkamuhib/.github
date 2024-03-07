import subprocess
import os

# Define your repository details
repo_name = "your-repository-name"
repo_dir = f"./{repo_name}"
file_name = "main.py"
remote_repo_url = "your-remote-repo-url"  # Replace with your GitHub repo URL
commit_message = "Initial commit"

# Function to run shell commands
def run_command(command, cwd=None):
    result = subprocess.run(command, cwd=cwd, shell=True, text=True, capture_output=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
    else:
        print(result.stdout)

# Create a new directory
