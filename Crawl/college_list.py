import requests
import re
from pyquery import PyQuery as pq
import pandas as pd
from Office.save_file import save_to_csv

def get_colleges():
    url = 'http://www.moe.gov.cn/jyb_zzjg/moe_347/201708/t20170828_312562.html'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/62.0'}
    res = requests.get(url, headers=headers)
    res.encoding = res.apparent_encoding
    data = res.text
    doc = pq(data)
    data = doc('.TRS_Editor table li').items()
    collegs = {}
    for d in data:
        name = d.text()
        website = d('a').attr('href')
        collegs[name] = website
    return collegs


res = get_colleges()
for k,v in res.items():
    li =[k,v]
    save_to_csv('colleges',li)