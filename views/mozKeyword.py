# -*- coding: utf-8 -*-
import sys, json
import urllib.request
import requests
from requests.auth import HTTPProxyAuth
import ast
from urllib.parse import unquote
# import urllib.parse as up
# from urllib.parse import quote

KEYWORDS_Moz = sys.stdin.read().split()
KEYWORDS_a = KEYWORDS_Moz[0].split(',')
# KEYWORDS_Moz_full = list(filter(None, KEYWORDS_Moz))
KEYWORDS_decode = []
KEYWORDS_full = []
# clean the search string
for elem in KEYWORDS_a:
    elem_decode = unquote(elem)
    elem_decode_a = elem_decode.replace(',', '')
    elem_decode_b = elem_decode_a.replace('\'', '')
    KEYWORDS_decode.append(elem_decode_b)

# remove empty string
for elem in KEYWORDS_decode:
    if elem != '':
        KEYWORDS_full.append(elem)


aa = []
bb = []
cc = []
dd = []
ee = []
ELE2 = [aa, bb, cc, dd, ee]

headers = {
    'X-Crawlera-Use-HTTPS': '1'
}

proxy_host = 'proxy.crawlera.com'
proxy_auth = HTTPProxyAuth('', '')
proxies = {
    'http': 'http://{}:8010/'.format(proxy_host)
}

# proxy_support = urllib.request.ProxyHandler(proxies)
# opener = urllib.request.build_opener(proxy_support)
# urllib.request.install_opener(opener)

for i in range(0, len(KEYWORDS_full)):
    try:
        r = requests.get('http://moz.com/explorer/api/2.4.2/keyword/suggestions/' + str(KEYWORDS_full[i]) + '?locale=zh-TW&strategy=default', headers=headers, proxies=proxies, auth=proxy_auth)
        resultJson = json.loads(r.text)
        resultJsonClean = resultJson['suggestions']
    except:
        ELE2[i].append('None')
        print(json.dumps(ELE2, ensure_ascii=False))
    else:
        for ele in resultJsonClean:
            ELE2[i].append(ele['keyword'])

print(json.dumps(ELE2, ensure_ascii=False))
