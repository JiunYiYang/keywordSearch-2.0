# -*- coding: utf-8 -*-
import sys, json
import urllib.request as ur
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

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36'}
for item in KEYWORDS_Moz_full:
    result = ur.urlopen('https://moz.com/explorer/api/2.2.7/keyword/suggestions/' + item + '?locale=en-US&strategy=default')
    resultJson = json.loads(result.read())
    resultJsonClean = resultJson['suggestions']
    for array in ELE2:
        array.append(item['keyword'])

print(json.dumps(ELE2, ensure_ascii=False))
