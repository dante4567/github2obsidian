import requests
import os

# Your GitHub username and personal access token
GITHUB_USERNAME = 'YOUR_GITHUB_USERNAME'
GITHUB_TOKEN = 'YOUR_GITHUB_TOKEN'
# Directory to save the Markdown files
OUTPUT_DIR = 'starred_repos_markdown'

headers = {'Authorization': f'token {GITHUB_TOKEN}'}

def fetch_starred_repos(username):
    """Fetch the starred repositories for the given GitHub username."""
    url = f'https://api.github.com/users/{username}/starred'
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raises an HTTPError if the response was an error
    return response.json()

def fetch_repo_readme(owner, repo_name):
    """Fetch the README content for a given repository."""
    url = f'https://api.github.com/repos/{owner}/{repo_name}/readme'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return requests.get(response.json()['download_url']).text
    return 'README not available.'

def save_markdown_file(repo_info):
    """Save the repository information in a Markdown file."""
    repo_name = repo_info['name']
    markdown_content = f"# {repo_name}\n\n"
    markdown_content += f"## Description\n{repo_info['description'] or 'No description.'}\n\n"
    markdown_content += f"## Tags\n{' '.join([f'- {tag}' for tag in repo_info['tags']])}\n\n"
    markdown_content += f"## README\n{repo_info['readme']}\n\n"
    markdown_content += f"## Star Count\n{repo_info['stargazers_count']}\n"

    file_path = os.path.join(OUTPUT_DIR, f"{repo_name.replace('/', '_')}.md")
    with open(file_path, 'w') as md_file:
        md_file.write(markdown_content)

if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    starred_repos = fetch_starred_repos(GITHUB_USERNAME)

    for repo in starred_repos:
        repo_info = {
            'name': repo['full_name'],
            'description': repo['description'],
            'tags': repo.get('topics', []),
            'stargazers_count': repo['stargazers_count'],
            'readme': fetch_repo_readme(repo['owner']['login'], repo['name'])
        }
        save_markdown_file(repo_info)

    print("Markdown files for starred repositories have been created.")
