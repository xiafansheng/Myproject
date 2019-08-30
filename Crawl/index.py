
import requests
from Office.save_file import save_to_csv

from pyquery import PyQuery as pq
import pandas as pd
from Office.maketime import nowtime
typelist = ['DE000SLA2514','DE000SLA0FS4','DE000SLA0RL4']
for t in typelist:
    url = 'https://www.solactive.com/indices/?indexhistory=%s&indexhistorytype=max'%t
    headers = {'Host': 'www.solactive.com', 'Connection': 'keep-alive', 'X-Requested-With': 'XMLHttpRequest',  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8', 'Accept': 'application/json, text/javascript, */*; q=0.01', 'Accept-Encoding': 'gzip, deflate, br', 'Cookie': 'cookieconsent_status=allow; _ga=GA1.2.764963108.1551520336; _gid=GA1.2.1014728705.1551520336; _gat=1', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36', 'Referer': 'https//www.solactive.com/indices/?index=DE000SLA4304'}
    html = requests.get(url,headers=headers)
    data = html.json()
    for d in data:
        date = nowtime(d['timestamp']/1000)
        li = [date]
        for k,v in d.items():
            li.append(v)
        save_to_csv('index',li)


# html = requests.post(url, headers=headers, data=data)
# doc = pq(html.text)