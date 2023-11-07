#!/usr/bin/python3
"""Defines a function that queries the Reddit API and prints the titles"""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts listed for a given subreddit"""
    url = 'https://oauth.reddit.com/r/{}/hot.json'.format(subreddit)
    user_agent = (
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        '(KHTML, like Gecko) '
        'Chrome/100.0.0.0 Safari/537.36'
    )

    headers = {'User-Agent': user_agent,
               'Authorization': (
                   'bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IlNIQTI1NjpzS3d'
                   'sMnlsV0VtMjVmcXhwTU'
                   '40cWY4MXE2OWFFdWFyMnpLMUdhVGxjdWNZIiwidHlwIjoiSldUI'
                   'n0.eyJzdWIiOiJ1c2Vy'
                   'IiwiZXhwIjoxNjk5NDQ5NDU1LjY4MDcwMSwiaWF0IjoxNjk5MzY'
                   'zMDU1LjY4MDcwMSwian'
                   'RpIjoiSGtJN01fWjRuYWE0NjZSeXNaVUxZd0d3X3kxTTJBIiwiY'
                   '2lkIjoiZlB3Q212OHBS'
                   'ZDJiNmVFcUR1SUxmdyIsImxpZCI6InQyX21wYnkyNXAzZyIsImF'
                   'pZCI6InQyX21wYnkyNX'
                   'AzZyIsImxjYSI6MTY5ODQ4NTIwNTI3OSwic2NwIjoiZUp5S1Z0S'
                   'lNpZ1VFQUFEX193TnpB'
                   'U2MiLCJmbG8iOjl9.WIuqlIGPbw8HJDyvuJBydFJGRVK-EZfJYG'
                   'ZuPWWkhlFXdcrGIXJen'
                   'SlWBvDxFFtzm7YOl-hnhqFzh4s9GI7H_kqyCegdogaYem5D8rRZ'
                   'rgc2tr4fyboprs1VXQm'
                   'RSfPul_CNaRF4kRdF7ZxzTC-MyaZf_rPLjudQATigpkaHObSyfi'
                   'YCBKKDVAygJqAVLHilq'
                   'mAUhGCiUvcfUPXuiA5UTCb-l2FJZfOahkv_3W4_aDxa1DT4qsYK'
                   'NiAsRtrLQwCAhwK8wLh'
                   'GtPU2lpKE2BTwUKheUduS0sDQgTuNH1O1e1Ec2areO7QPlXTJk7'
                   '5154QqOB_WjtceobA3NfxUaZUsVA'
               )
               }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        posts = response.json().get('data').get('children')
        for post in posts[:10]:
            print(post.get('data').get('title'))

    else:
        print('None')
