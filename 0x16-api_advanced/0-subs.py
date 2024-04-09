#!/usr/bin/python3
'''
Make api request to reddit to get the number of subscribers
in a sub-reddit
'''
import requests


def number_of_subscribers(subreddit):
    '''Retrieve the number of subscribers'''
    res = requests.get(f'https://reddit.com/r/{subreddit}/about.json')
    if (res.status_code == 200):
        # print subscriber count
        try:
            return res.json()['data']['subscribers']
        except KeyError:
            return 0
