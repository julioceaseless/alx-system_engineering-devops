#!/usr/bin/python3
"""
Query Reddit API to parse the list of hot articles
and print a sorted count of given keywords
"""

import requests


def count_words(subreddit, word_list, found_list=[], after=None):
    """
    Prints counts of given words found in hot posts of a given subreddit.
    """
    headers = {'User-agent': 'myApp/v1.0.1'}
    res = requests.get('http://www.reddit.com/r/{}/hot.json?after={}'
                       .format(subreddit, after), headers=headers)
    if after is None:
        word_list = [word.lower() for word in word_list]

    if res.status_code == 200:
        aft = res.json().get('data').get('after')
        posts = res.json().get('data').get('children')
        for post in posts:
            title = post['data']['title'].lower()
            for word in title.split(' '):
                if word in word_list:
                    found_list.append(word)
        if aft is not None:
            count_words(subreddit, word_list, found_list, aft)
        else:
            result = {}
            for word in found_list:
                if word.lower() in result.keys():
                    result[word.lower()] += 1
                else:
                    result[word.lower()] = 1
            for key, value in sorted(result.items(), key=lambda item: item[1],
                                     reverse=True):
                print('{}: {}'.format(key, value))
    else:
        return
