#!/usr/bin/python3
"""
Function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    for a given subreddit.
    If not a valid subreddit, print None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    params = {"limit": 10}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code == 200:
        posts = response.json().get("data", {}).get("children", [])
        for post in posts:
            print(post["data"]["title"])
    else:
        print(None)