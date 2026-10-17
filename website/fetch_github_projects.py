"""Fetch public GitHub repositories and recent releases for a user and write them to website/data/github_projects.json

This script uses the unauthenticated GitHub API and is intended to be run in CI or locally.
"""
from pathlib import Path
import json
import urllib.request
import urllib.error
import os
import time

GITHUB_USER = os.environ.get("GITHUB_USER", "chadwickcjohnson-sketch")
OUTPUT_PATH = Path(os.environ.get("GITHUB_PROJECTS_OUTPUT", "website/data/github_projects.json"))
API_BASE = "https://api.github.com"


def _get_json(url: str):
    req = urllib.request.Request(url, headers={"User-Agent": "Galaxigates-Site-Build/1.0"})
    try:
        with urllib.request.urlopen(req) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        # Rate limit or not found
        print(f"HTTPError for {url}: {e.code}")
        return None
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None


def fetch_repos(user: str):
    repos = []
    page = 1
    per_page = 100
    while True:
        url = f"{API_BASE}/users/{user}/repos?per_page={per_page}&page={page}&sort=updated"
        data = _get_json(url)
        if not data:
            break
        repos.extend(data)
        if len(data) < per_page:
            break
        page += 1
        time.sleep(0.5)
    return repos


def fetch_latest_release(owner: str, repo: str):
    url = f"{API_BASE}/repos/{owner}/{repo}/releases/latest"
    return _get_json(url)


def build_projects_payload(user: str):
    raw = fetch_repos(user)
    projects = []
    for r in raw:
        proj = {
            "name": r.get("name"),
            "full_name": r.get("full_name"),
            "html_url": r.get("html_url"),
            "description": r.get("description"),
            "language": r.get("language"),
            "stars": r.get("stargazers_count", 0),
            "updated_at": r.get("updated_at"),
        }
        release = fetch_latest_release(r.get("owner", {}).get("login", user), r.get("name"))
        if release and isinstance(release, dict):
            proj["latest_release"] = {
                "tag_name": release.get("tag_name"),
                "name": release.get("name"),
                "published_at": release.get("published_at"),
                "html_url": release.get("html_url"),
            }
        projects.append(proj)
        time.sleep(0.2)
    return projects


def main():
    out_dir = OUTPUT_PATH.parent
    out_dir.mkdir(parents=True, exist_ok=True)
    projects = build_projects_payload(GITHUB_USER)
    payload = {"generated_at": os.environ.get("BUILD_TIME" , ""), "projects": projects}
    with OUTPUT_PATH.open("w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)
    print(f"Wrote {len(projects)} projects to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
