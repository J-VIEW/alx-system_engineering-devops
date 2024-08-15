#!/usr/bin/python3
"""
Recursive function that queries the Reddit API and returns
a list containing the titles of all hot articles for a given subreddit.
If no results are found for the given subreddit,
the function should return None.
"""

import requests


def recurse(subreddit, hot_list=None, after=None):
    """
    Queries the Reddit API and returns
    a list containing the titles of all hot articles for a given subreddit.

    - If not a valid subreddit, return None.
    """
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Custom User Agent"}
    params = {"limit": 100, "after": after}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        
        if response.status_code != 200:
            return None

        data = response.json()
        posts = data['data']['children']

        if not posts:
            return hot_list if hot_list else None

        for post in posts:
            hot_list.append(post['data']['title'])

        after = data['data']['after']
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list

    except Exception:
        return None