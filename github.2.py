import requests
from github import Github

# Your GitHub Personal Access Token
token = "your_token_here"

# Set up `requests` authentication
headers = {'Authorization': 'token ' + token}

# Set up `PyGithub` authentication
gh = Github(token)
