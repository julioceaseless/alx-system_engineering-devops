#!/usr/bin/python3
'''
Make api request to reddit to get the number of subscribers
in a sub-reddit
'''
import requests


def number_of_subscribers(subreddit):
    '''Retrieve the number of subscribers'''
    headers = {'User-Agent': 'app/v1.0.0'}
    url = "https://reddit.com/r/{}/about.json".format(subreddit)
    res = requests.get(url, headers=headers, allow_redirects=False)
    if (res.status_code == 200 and not res.is_redirect):
        # print subscriber count
        try:
            return int(res.json()['data']['subscribers'])
        except KeyError:
            return 0
    else:
        return 0
