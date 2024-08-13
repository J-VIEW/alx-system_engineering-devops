#!/usr/bin/python3
"""
Function that queries the Reddit API and prints the titles of the first 10 hot posts
listed for a given subreddit.
"""

import requests

def top_ten(subreddit):
    """
    Query the Reddit API to get the titles of the first 10 hot posts for a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit.
    
    Prints:
        The titles of the first 10 hot posts, or None if the subreddit is invalid or an error occurs.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Python/requests"}
    params = {"limit": 10}
    
    try:
        response = requests.get(url, headers=headers, params=params, timeout=5)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        data = response.json()
        posts = data["data"]["children"]
        
        for post in posts:
            print(post["data"]["title"])
    except (requests.RequestException, KeyError, ValueError):
        print(None)