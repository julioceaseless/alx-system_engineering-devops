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

    # perform GET request to API without following redirect
    res = requests.get(url, headers=headers, allow_redirects=False)
    if (res.status_code == 200):
        # print the number of subscribers
        data = res.json().get('data', {})
        subscribers = data.get('subscribers', 0)
        return subscribers
    else:
        return 0
