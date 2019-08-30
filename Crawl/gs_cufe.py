import requests
from pyquery import PyQuery as pq
import pandas as pd
import tabula

data = requests.get('http://gs.cufe.edu.cn/info/1050/5479.htm')
data.encoding = data.apparent_encoding
doc = pq(data.text)
res = doc('a').items()
for r in res:
    if 150<len(str(r))<200:
        try:
             name = r.text()

            link = 'http://gs.cufe.edu.cn'+r.attr('href')
            df = tabula.read_pdf(link,encoding = 'utf-8',pages='all')
            result = first.append(df)
            #df.to_excel('%s.xls'%name,encoding='utf-8')
        except:
            pass
all.to_excel('admitted.xls',encoding='utf-8')