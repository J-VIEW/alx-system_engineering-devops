#!/usr/bin/python3
"""
Recursive function that queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit. If no results are found
for the given subreddit, the function should return None.
"""
import requests

def recurse(subreddit, hot_list=None, after=None, count=0):
    """
    Recursively query the Reddit API to get all hot articles for a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): List to store the titles of hot articles (default is None).
        after (str): Token for pagination (default is None).
        count (int): Number of items already retrieved (default is 0).
    
    Returns:
        list: A list of titles of all hot articles, or None if the subreddit is invalid.
    """
    if hot_list is None:
        hot_list = []
    
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Python/requests"}
    params = {"after": after, "count": count, "limit": 100}
    
    try:
        response = requests.get(url, headers=headers, params=params, timeout=5)
        response.raise_for_status()
        
        data = response.json()["data"]
        
        new_posts = [post["data"]["title"] for post in data["children"]]
        hot_list.extend(new_posts)
        
        if data["after"]:
            return recurse(subreddit, hot_list, data["after"], count + len(new_posts))
        else:
            return hot_list if hot_list else None
    except (requests.RequestException, KeyError, ValueError):
        return None if not hot_list else hot_list