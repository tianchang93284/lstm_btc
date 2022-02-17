import http.client
import json
import pandas as pd

import requests
url = 'https://okexweb.loongshop.cn/api/v5/market/history-candles?instId=BTC-USDT'
r = requests.get(url, headers = { 'Accept' : 'application/json' })
print(r.text)#[()[ 'data''data' ][][ 'avg''avg' ][][ 'display_short''display_short' ]

