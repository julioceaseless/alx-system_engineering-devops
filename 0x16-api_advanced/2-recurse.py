#!/usr/bin/python3
"""
Recursive function queries the Reddit API and returns
a list of titles of all hot articles for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Returns a list of titles of all hot posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {"User-Agent": "app/v1.0.0"}
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    res = requests.get(url, headers=headers, params=params,
                       allow_redirects=False)
    if res.status_code != 200:
        return None

    results = res.json()['data']
    after = results['after']
    count += results['dist']
    for c in results['children']:
        hot_list.append(c['data']['title'])

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
