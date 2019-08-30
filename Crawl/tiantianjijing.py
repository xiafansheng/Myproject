from pyquery import PyQuery as pq
import requests
from Crawl.get_cookie_header import get_headers
import pandas as pd
import time
#
url = 'http://api.fund.eastmoney.com/f10/lsjz?callback=jQuery18309759651385273642_1552467335645&fundCode=000198&pageIndex=1&pageSize=20&startDate=&endDate=&_=%s'%time.time()

headers = get_headers('ttjj.txt')
res = requests.get(url, headers=headers)
res.encoding = res.apparent_encoding
data = res.text
print(data)
#doc = pq(data)
# res = data['Datas']['Datas']
# df = pd.DataFrame(res)
# df.to_excel('货币型.xlsx')
# print(df)
