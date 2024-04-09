#!/usr/bin/python3
'''
Script queries Reddit API and prints the titles of the
first 10 hot posts listed for a given subreddit
'''
import requests


def top_ten(subreddit):
    '''List 10 hot posts'''
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'app/v1.00', 'Cache-Control': 'no-cache'}
    res = requests.get(url, headers=headers, allow_redirects=False)
    if (res.status_code == 200 and not res.is_redirect):
        try:
            dict_list = res.json()['data']['children']
            for i in range(10):
                print(dict_list[i]['data']['title'])
        except Exception as e:
            print("None")
    else:
        print("None")
