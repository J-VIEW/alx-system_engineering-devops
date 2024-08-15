#!/usr/bin/python3
""" Module for storing the count_words function. """
import requests
import re

def count_words(subreddit, word_list, after=None, word_count=None):
    """
    Recursively queries the Reddit API, parses the titles of hot articles,
    and prints a sorted count of given keywords.
    """
    if word_count is None:
        word_count = {}
        for word in word_list:
            word_count[word.lower()] = 0

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Custom User Agent'}
    params = {'limit': 100, 'after': after}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        
        if response.status_code != 200:
            return

        data = response.json()
        posts = data['data']['children']

        for post in posts:
            title = post['data']['title'].lower()
            words = re.findall(r'\b[\w]+\b', title)
            
            for word in words:
                if word in word_count:
                    word_count[word] += 1

        after = data['data']['after']
        if after:
            count_words(subreddit, word_list, after, word_count)
        else:
            sorted_counts = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                if count > 0:
                    print(f"{word}: {count}")

    except Exception:
        return

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        count_words(sys.argv[1], [x.lower() for x in sys.argv[2].split()])