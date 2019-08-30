import requests
import json
import pandas as pd


url="https://www.adidas.com.cn/location/storelist.json?startPage=1&size=12"
html = requests.get(url).text
result=json.loads(html)
storelist=result['storeMapResult']
sts = []
for store in storelist:
    st={'brand':'adidas'}
    st['province']=store['province']
    st['city'] = store['city']
    st['pOSNameCN']=store['pOSNameCN']
    st['addressCN']=store['addressCN']
    st['telephone']=store['telephone']
    st['storeType']=store['storeType']
    sts.append(st)
df = pd.DataFrame(sts)
df.to_excel('adidas.xlsx')

