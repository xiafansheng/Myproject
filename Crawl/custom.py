import requests
import re
from pyquery import PyQuery as pq
import pandas as pd

def get_link(texts):
    text = re.findall(' <tr>(.*?)口商品类章金额表</td> (.*?)</tr> ',texts,re.S)
    return  text

def get_linkmonth(texts):
    text = re.findall('href="(.*?)" target="blank" > (.*?)月',texts,re.S)
    return text

def get_title(texts):
    text = re.findall('<td style="TEXT-INDENT: 5px">(.*?)',texts,re.S)

def getinfo():
    info = []
    url = 'http://www.customs.gov.cn/customs/302249/302274/302277/index.html'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/62.0'}
    res = requests.get(url, headers=headers)
    data = res.text
    doc = pq(data)
    link = get_link(str(doc))
    for l in link:
        title = l[0].split('5px">')[-1]
        docs = pq(l[1])
        a = docs('td a').items()
        for l in a:
            links = l.attr('href')
            month = l.text()
            #titles = str(title) + link
            if links:
                info.append([title,month,links])
    return info

def savetoxls(url,ty,mo,ye):
    data = pd.read_html(url)[0]
    country =[x for x in  data.ix[[1],:].values[0] if str(x) != 'nan'][1:]
    month = [x for x in data.ix[[2],:].values[0] if str(x) !='nan'][:2]
    names = ['类章']
    columns = [[i+month[0],i+month[1]] for i in country]
    for i in columns:
        names = names+i
    df = data.ix[3:,:]
    df.columns = names
    df['type'] = ty
    df['year'] = ye
    df['month'] = mo
    return df
data = getinfo()
index = []
for i in data:
    index.append(i)
di = pd.DataFrame(index)
di.to_excel('index.xls')
