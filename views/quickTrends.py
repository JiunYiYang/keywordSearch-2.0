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

# get search conditions
KEYWORD = sys.stdin.read()
GEO = sys.stdin.read()

# get trends data
pytrend = TrendReq(hl='en-US', tz=360)
pytrend.build_payload(kw_list=KEYWORD, cat=0, timeframe='today 12-m', geo=GEO, gprop='')
if pytrend.interest_over_time().get(KEYWORD) is not None:
    preload = json.loads(pytrend.interest_over_time().get(KEYWORD).to_json(orient='table'))['data']
    print(json.dumps(preload, ensure_ascii=False))

else:
    print('none')
