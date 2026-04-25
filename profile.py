import requests

def fetch_repos(username):
    # Mengambil semua repo publik
    url = f"https://api.github.com/users/{username}/repos?sort=updated&per_page=10"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return []

def generate_markdown(repos):
    header = "| Proyek | Deskripsi | Stack |\n|--------|-----------|-------|\n"
    rows = []
    for repo in repos:
        # Filter: Bukan fork dan punya deskripsi
        if not repo['fork'] and repo['description']:
            name = repo['name']
            # Gunakan homepage/website jika ada, kalau tidak ada pakai link github
            link = repo['homepage'] if repo['homepage'] else repo['html_url']
            desc = repo['description']
            lang = repo['language'] if repo['language'] else "Misc"
            
            rows.append(f"| [**{name}**]({link}) | {desc} | `{lang}` |")
    
    return header + "\n".join(rows)

def update_readme(content):
    with open("README.md", "r", encoding="utf-8") as f:
        readme = f.read()

    start_tag = ""
    end_tag = ""
    
    if start_tag in readme and end_tag in readme:
        before = readme.split(start_tag)[0]
        after = readme.split(end_tag)[1]
        new_readme = f"{before}{start_tag}\n{content}\n{end_tag}{after}"
        
        with open("README.md", "w", encoding="utf-8") as f:
            f.write(new_readme)

if __name__ == "__main__":
    # Pakai username kamu
    user = "cdn-lib" 
    data = fetch_repos(user)
    if data:
        table = generate_markdown(data)
        update_readme(table)
