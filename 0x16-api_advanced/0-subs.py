#!/usr/bin/python3
"""Defines a function that queries the Reddit API and returns the number of subscrivers for a given subreddit"""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit"""
    url = 'https://oauth.reddit.com/r/{}/about.json'.format(
        subreddit)
    user_agent = (
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/100.0.0.0 Safari/537.36'
    )

    headers = {'User-Agent': user_agent,
               'Authorization': (
                   'bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IlNIQTI1NjpzS3dsMnlsV0VtMjVmcXhwTU'
                   '40cWY4MXE2OWFFdWFyMnpLMUdhVGxjdWNZIiwidHlwIjoiSldUIn0.eyJzdWIiOiJ1c2Vy'
                   'IiwiZXhwIjoxNjk5NDQ5NDU1LjY4MDcwMSwiaWF0IjoxNjk5MzYzMDU1LjY4MDcwMSwian'
                   'RpIjoiSGtJN01fWjRuYWE0NjZSeXNaVUxZd0d3X3kxTTJBIiwiY2lkIjoiZlB3Q212OHBS'
                   'ZDJiNmVFcUR1SUxmdyIsImxpZCI6InQyX21wYnkyNXAzZyIsImFpZCI6InQyX21wYnkyNX'
                   'AzZyIsImxjYSI6MTY5ODQ4NTIwNTI3OSwic2NwIjoiZUp5S1Z0SlNpZ1VFQUFEX193TnpB'
                   'U2MiLCJmbG8iOjl9.WIuqlIGPbw8HJDyvuJBydFJGRVK-EZfJYGZuPWWkhlFXdcrGIXJen'
                   'SlWBvDxFFtzm7YOl-hnhqFzh4s9GI7H_kqyCegdogaYem5D8rRZrgc2tr4fyboprs1VXQm'
                   'RSfPul_CNaRF4kRdF7ZxzTC-MyaZf_rPLjudQATigpkaHObSyfiYCBKKDVAygJqAVLHilq'
                   'mAUhGCiUvcfUPXuiA5UTCb-l2FJZfOahkv_3W4_aDxa1DT4qsYKNiAsRtrLQwCAhwK8wLh'
                   'GtPU2lpKE2BTwUKheUduS0sDQgTuNH1O1e1Ec2areO7QPlXTJk75154QqOB_WjtceobA3NfxUaZUsVA'
               )
               }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get('data').get('subscribers')
    else:
        return 0
