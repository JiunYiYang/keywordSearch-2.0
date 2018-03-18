
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

KEYWORDS = sys.stdin.read().split()
KEYWORDS = KEYWORDS[0].split(',')
KEYWORDS_full = list(filter(None, KEYWORDS))

# Login to Google. Only need to run this once, the rest of requests will use the same session.
pytrend = TrendReq(hl='en-US', tz=360)

# Create payload and capture API tokens. Only needed for interest_over_time(), interest_by_region() & related_queries()
pytrend.build_payload(kw_list=KEYWORDS_full, cat=0, timeframe='today 12-m', geo='', gprop='')

# get worldwide trends data
if pytrend.interest_over_time().get(KEYWORDS_full) is not None:
    worldTrends = json.loads(pytrend.interest_over_time().get(KEYWORDS_full).to_json(orient='table'))['data']
    # worldTrends = json.dumps(preload, ensure_ascii=False)

else:
    worldTrends = []


# sort by country order by volume dividly extract, and add to list
aa = []
bb = []
cc = []
dd = []
ee = []
top5Regions = [aa, bb, cc, dd, ee]
for i in range(0, len(KEYWORDS_full)):
    potentialTopRegions = pytrend.interest_by_region(resolution='COUNTRY').sort_values(by=KEYWORDS_full[i], ascending=False)
    potentialTopRegions = json.loads(potentialTopRegions.get(KEYWORDS_full[i]).to_json(orient='table'))['data']
    for region in potentialTopRegions:
        for country in Country:
            if region['geoName'] in country:
                top5Regions[i].append({
                    'geoName': region['geoName'],
                    KEYWORDS_full[i]: region[KEYWORDS_full[i]],
                    'geoCode': country[0]
                })

# if top5Regions is not None:
#     top5Regions = json.dumps(top5Regions, ensure_ascii=False)

# else:
#     top5Regions = 'none'


# return results
total = [worldTrends, top5Regions]
print(json.dumps(total, ensure_ascii=False))
