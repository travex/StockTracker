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

if __name__ == '__main__':
    TwitterKeys = load_keys("twitterAPIKeys.yaml")
    print(TwitterKeys['BearerToken'])