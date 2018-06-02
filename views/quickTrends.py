from pytrends.request import TrendReq
from countryCode import Country
import time
import sys
import os
import json
from random import randint
import numpy as np
import pandas as pd
from pandas import DataFrame
from requests.auth import HTTPProxyAuth

# get search conditions
INPUT = sys.stdin.readline()
INPUT = json.loads(INPUT)

# pytrends with proxies
proxy_host = 'proxy.crawlera.com'
proxy_auth = HTTPProxyAuth('', '')
proxies = {
    'http': 'http://{}:8010/'.format(proxy_host)
}

# get trends data
pytrend = TrendReq(hl='en-US', tz=360, proxies=proxies)
pytrend.build_payload(kw_list=[INPUT['keyword']], cat=0, timeframe='today 12-m', geo=INPUT['country'], gprop='')
if pytrend.interest_over_time().get(INPUT['keyword']) is not None:
    preload = json.loads(pytrend.interest_over_time().get(INPUT['keyword']).to_json(orient='table'))['data']
    print(json.dumps(preload, ensure_ascii=False))

else:
    print('none')
