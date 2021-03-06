import requests as rq
import pandas as pd
import sys
import ast
import json
import yaml


def load_keys(filename):
    with open(filename) as f:
        keys = yaml.safe_load(f)
    return keys

def create_url(url_type, key, tweet_count = 100):
    tweet_fields = "tweet.fields=lang,author_id"

    #ids = "ids=1278747501642657792,1255542774432063488"
    mvis = "mvis"
    keyword = {"M": "mvis AND -$mvis", "T":"tesla OR tsla"}

    list_url = {"RecentV2":"https://api.twitter.com/2/tweets/search/recent?query=",
                "TweetsV1":"https://api.twitter.com/1.1/search/tweets.json?q="}
    url = list_url[url_type] + keyword[key] + "&count={}".format(tweet_count)
    return url


def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers


def connect_to_endpoint(url, headers):
    response = rq.request("GET", url, headers=headers)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()

if __name__ == '__main__':
    TwitterKeys = load_keys("twitterAPIKeys.yaml")
    consumer_key = TwitterKeys['APIKey']
    consumer_secret = TwitterKeys['APISecretKey']
    bearer_token = TwitterKeys['BearerToken']

    url = create_url("TweetsV1","M",1)
    data = connect_to_endpoint(url, create_headers(bearer_token))
    print(json.dumps(data, indent=4, sort_keys=True))
