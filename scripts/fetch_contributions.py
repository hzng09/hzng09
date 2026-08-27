import sys
import json
import requests
from bs4 import BeautifulSoup

def fetch_contributions(username):
    url = f"https://github.com/users/{username}/contributions"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    resp = requests.get(url, headers=headers)
    if resp.status_code != 200:
        print(f"Error fetching contributions for {username}: HTTP {resp.status_code}")
        sys.exit(1)
        
    soup = BeautifulSoup(resp.text, 'html.parser')
    days = []
    
    for td in soup.find_all(['td', 'tool-tip']):
        date = td.get('data-date')
        level = td.get('data-level')
        if date and level is not None:
            days.append({'date': date, 'level': int(level)})
            
    output_path = "data/contributions.json"
    with open(output_path, "w") as f:
        json.dump({"username": username, "days": days}, f, indent=2)
    print(f"Saved {len(days)} contribution days for '{username}' to {output_path}")

if __name__ == "__main__":
    username = sys.argv[1] if len(sys.argv) > 1 else "octocat"
    fetch_contributions(username)
