# -*- coding: utf-8 -*-
import sys, json
from urllib.request import Request, urlopen
import ast
# import urllib.parse as up
# from urllib.parse import quote

KEYWORDS_Moz = sys.stdin.read().split()
KEYWORDS_Moz = KEYWORDS_Moz[0].split(',')
KEYWORDS_Moz_full = list(filter(None, KEYWORDS_Moz))

aa = []
bb = []
cc = []
dd = []
ee = []
ELE2 = [aa, bb, cc, dd, ee]

hdr = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'User-Agent': 'cheese',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive'
}

for i in range(0, len(KEYWORDS_Moz_full)):
    req = Request('https://moz.com/explorer/api/2.2.7/keyword/suggestions/' + KEYWORDS_Moz_full[i] + '?locale=en-US&strategy=default', headers=hdr)
    result = urlopen(req).read()
    resultJson = json.loads(result.decode('utf-8'))
    resultJsonClean = resultJson['suggestions']
    for ele in resultJsonClean:
        ELE2[i].append(ele['keyword'])

print(json.dumps(ELE2, ensure_ascii=False))
