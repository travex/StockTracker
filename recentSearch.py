import requests as rq
import json
import yaml

def load_keys(filename):
    with open(filename) as f:
        keys = yaml.safe_load(f)
    return keys

#define search twitter function
def search_twitter(query, tweet_fields, bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}

    url = "https://api.twitter.com/2/tweets/search/recent?query={}&{}".format(query, tweet_fields)
    response = rq.request("GET", url, headers=headers)

    print(response.status_code)

    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()

if __name__ == '__main__':
    TwitterKeys = load_keys("twitterAPIKeys.yaml")
    consumer_key = TwitterKeys['APIKey']
    consumer_secret = TwitterKeys['APISecretKey']
    bearer_token = TwitterKeys['BearerToken']

    # search term
    query = "MVIS"

    # twitter fields to be returned by api call
    tweet_fields = "tweet.fields=text,author_id,created_at"

    # twitter api call
    json_response = search_twitter(query=query, tweet_fields=tweet_fields, bearer_token=bearer_token)

    # pretty printing
    print(json.dumps(json_response, indent=4, sort_keys=True))