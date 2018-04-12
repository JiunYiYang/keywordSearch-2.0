# -*- coding: utf-8 -*-
import sys, json
from urllib.request import Request, urlopen, ProxyHandler, build_opener, install_opener
import requests
from requests.auth import HTTPProxyAuth
import ast
from urllib.parse import unquote
# import logging
# logging.basicConfig(level=logging.DEBUG)
# import urllib.parse as up
# from urllib.parse import quote

KEYWORDS_Moz = sys.stdin.read().split()
KEYWORDS_Moz = KEYWORDS_Moz[0].split(',')
KEYWORDS_Moz_full = list(filter(None, KEYWORDS_Moz))
# KEYWORDS_decode = []
# KEYWORDS_full = []
# # clean the search string
# for elem in KEYWORDS_a:
#     elem_decode = unquote(elem)
#     elem_decode_a = elem_decode.replace(',', '')
#     elem_decode_b = elem_decode_a.replace('\'', '')
#     KEYWORDS_decode.append(elem_decode_b)

# # remove empty string
# for elem in KEYWORDS_decode:
#     if elem != '':
#         KEYWORDS_full.append(elem)

# logging.debug(KEYWORDS_Moz_full)

aa = []
bb = []
cc = []
dd = []
ee = []
ELE2 = [aa, bb, cc, dd, ee]

# hdr = {
#     'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
#     'User-Agent': 'cheese',
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#     'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
#     'Accept-Encoding': 'none',
#     'Accept-Language': 'en-US,en;q=0.8',
#     'Connection': 'keep-alive'
# }

# hdr = {
#     'X-Crawlera-Use-HTTPS': 1
# }

headers = {
    'X-Crawlera-Use-HTTPS': '1'
}

proxy_host = 'proxy.crawlera.com'
proxy_auth = HTTPProxyAuth('11446374f3a44394ae6165761d9055fd', '')
proxies = {
    'http': 'http://{}:8010/'.format(proxy_host)
}

# proxy_support = ProxyHandler(proxies)
# opener = build_opener(proxy_support)
# install_opener(opener)

for i in range(0, len(KEYWORDS_Moz_full)):
    try:
        r = requests.get('https://moz.com/explorer/api/2.3.0/keyword/suggestions/' + KEYWORDS_Moz_full[i] + '?locale=en-US&strategy=default', headers=headers, proxies=proxies, auth=proxy_auth)
        # req = Request('https://moz.com/explorer/api/2.2.7/keyword/suggestions/' + KEYWORDS_Moz_full[i] + '?locale=en-US&strategy=default', headers=hdr)
        # with urlopen(req) as response:
        #     result = response.read()
        #     resultJson = json.loads(result.decode('utf-8'))
        #     resultJsonClean = resultJson['suggestions']
        resultJson = json.loads(r.text)
        resultJsonClean = resultJson['suggestions']
    except KeyError:
        ELE2[i].append('None')
    else:
        for ele in resultJsonClean:
            ELE2[i].append(ele['keyword'])

print(json.dumps(ELE2, ensure_ascii=False))
