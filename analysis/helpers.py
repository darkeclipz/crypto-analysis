import time
import datetime
import requests
import json

def get_unix_time_minus_days(subtract_days):
    return int(time.time())-(86400*subtract_days)

def parse_unix_date(posix_time):
    return datetime.datetime.utcfromtimestamp(posix_time).strftime('%Y-%m-%dT%H:%M:%SZ')

def http_get(url):
    r = requests.get(url)
    data = json.loads(r.text)
    return data
